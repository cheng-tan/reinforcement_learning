import subprocess
import multiprocessing
import logging
import os


def _cache(vw_path, input, output):
    opts = {}
    opts['-d'] = input
    opts['--cache_file'] = output
    return (opts, run(build_command(vw_path, '', opts)))

def _cache_func(input):
    return _cache(input[0], input[1], input[2])

def _cache_multi(vw_path, inputs, output_path_gen, pool):
    inputs = list(map(lambda i: (vw_path, i, output_path_gen.get(i, 'cache')), inputs))
    result = pool.map(_cache_func, inputs)
    return result

def _train(vw_path, cache_file, model_file, opts = {}):
    opts['--cache_file'] = cache_file
    opts['-f'] = model_file
    return (opts, run(build_command(vw_path, '', opts)))

def _train_func(input):
    return _train(input[0], input[1], input[2], input[3])

def _train_multi(vw_path, cache_files, model_path_gen, opts, pool):
    previous = [(None, None)] * len(opts) 
    for c in cache_files:
        inputs = list(map(lambda o: (vw_path, c, model_path_gen.get(c, str(_hash('', o)) + '.vw'), o), opts))
        result = pool.map(_train_func, inputs)
        opts = list(map(lambda r: r[0], result))
        for o in opts:
            o['-i'] = o['-f']
    return result

def _parse_vw_output(txt):
    result = {}
    for line in txt.split('\n'):
        if '=' in line:
            index = line.find('=')
            key = line[0:index].strip()
            value = line[index+1:].strip()
            result[key] = value
    return result

def _hash(command='', opts={}):
    for key, val in opts.items():
        command = ' '.join([
            command,
            key,
            val
        ])

    return hash(command)

def run(command):
    print('Running the command: ' + command)
    process = subprocess.Popen(
        command.split(),
        universal_newlines=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    output, error = process.communicate()
    return _parse_vw_output(error)


def build_command(vw_path, command='', opts={}):
    if command:
        command = ' '.join([
            vw_path,
            command,
            '--save_resume',
            '--preserve_performance_counters'
        ])
    else:
        command = ' '.join([
            vw_path,
            '--cb_adf',
            '--dsjson',
            '--save_resume',
            '--preserve_performance_counters'
        ])

    for key, val in opts.items():
        command = ' '.join([
            command,
            key,
            str(val)
        ])
    return command

def cache(vw_path, input, output_path_gen, opts = {}, procs = 1):
    if not isinstance(input, list):
        input = [input]
    p = multiprocessing.Pool(procs)
    result = _cache_multi(vw_path, input, output_path_gen, p)
    p.close()
    p.join()
    return list(map(lambda r: r[0]['--cache_file'], result))

def train(vw_path, cache, model_path_gen, opts = {}, procs = 1):
    if not isinstance(opts, list):
        opts = [opts]
    
    if not isinstance(cache, list):
        cache = [cache]

    p = multiprocessing.Pool(procs)
    result = _train_multi(vw_path, cache, model_path_gen, opts, p)
    p.close()
    p.join()
    for r in result:
        r[0].pop('-f', None)
        r[0].pop('-i', None)
        r[0].pop('--cache_file', None)
    return list(map(lambda r: (r[0], r[1]['average loss']), result))

if __name__ == '__main__':
    multiprocessing.freeze_support()

