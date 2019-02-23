# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.
import argparse
import os
import datetime
import shutil

def datetime_2_subfolder(dt):
    return 'data/' + str(dt.year) + '/' + str(dt.month).zfill(2) + '/' + str(dt.day).zfill(2) + '_0.json'

class logs_entry:
    def __init__(self, file_name, start_datetime = datetime.datetime.min, end_datetime=datetime.datetime.max):
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.file_name = file_name
    
    def is_cutoff_needed(self):
        return self.start_datetime != datetime.datetime.min or self.end_datetime != datetime.datetime.max

def is_same_day(first, second):
    return first.year == second.year and first.month == second.month and first.day == second.day

def ds_timestamp_parse(ds_timestamp):
    return datetime.datetime.strptime(ds_timestamp, "%Y-%m-%dT%H:%M:%S.%f0Z")

def get_timestamp(dsline):
    position = dsline.find('Timestamp')
    if position == -1:
        return None

    datetimeStart = position + 12
    datetimeEnd = dsline.find('"', datetimeStart)
    return ds_timestamp_parse(dsline[datetimeStart:datetimeEnd])

def is_good_for_train(line):
    return line is not None and line.startswith('{"_label_cost') or line.startswith('{"o":') or line.startswith('{"Timestamp"')

def handle_log_file_to_1_file(input_log_entry, fout):
    if (os.path.isfile(input_log_entry.file_name)):
        if input_log_entry.is_cutoff_needed():
            print('Copying with cutoff: ' + input_log_entry.file_name)
            with open(input_log_entry.file_name, 'r') as fin:
                for line in fin:
                    ts = get_timestamp(line)
                    if ts is not None and input_log_entry.start_datetime <= ts and ts < input_log_entry.end_datetime and is_good_for_train(line):
                        fout.write(line)
        else:
            print('Copying without cutoff: ' + input_log_entry.file_name)
            with open(input_log_entry.file_name, 'r') as fin:
                for line in fin:
                    if is_good_for_train(line):
                        fout.write(line)
    else:
        print('Cannot find file: ' + input_log_entry.file_name)


def iterate_ds_logs(start_datetime, end_datetime):
    start_date = datetime.datetime(start_datetime.year, start_datetime.month, start_datetime.day)
    end_date = datetime.datetime(end_datetime.year, end_datetime.month, end_datetime.day)

    for d in (start_date + datetime.timedelta(i) for i in range((end_date - start_date).days + 1)):
        s = start_datetime if is_same_day(d, start_datetime) else datetime.datetime.min
        e = end_datetime if is_same_day(d, end_datetime) else datetime.datetime.max
        yield logs_entry(datetime_2_subfolder(d), s, e)
        
def extract_batches_to_1_file(input_folder, start_datetime, end_datetime, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, 'dataset.json')
    with open(output_path, 'w') as fout:
        for ds_entry in iterate_ds_logs(start_datetime, end_datetime):
            ds_entry.file_name = os.path.join(input_folder, ds_entry.file_name)
            print('Processing log file: ' + ds_entry.file_name)
            handle_log_file_to_1_file(ds_entry, fout)

print("Extracting data from application logs...")

parser = argparse.ArgumentParser("train")
parser.add_argument("--input_folder", type=str, help="input folder")
parser.add_argument("--output_folder", type=str, help="output folder")
parser.add_argument("--start_datetime", type=str, help="start datetime of batch")
parser.add_argument("--end_datetime", type=str, help="end datetime of batch")
parser.add_argument("--pattern", type=str, help="date time parsing pattern")
args = parser.parse_args()

print("Argument 1: %s" % args.input_folder)
print("Argument 2: %s" % args.output_folder)
print("Argument 3: %s" % args.start_datetime)
print("Argument 4: %s" % args.end_datetime)
print("Argument 5: %s" % args.pattern)

start_datetime = datetime.datetime.strptime(args.start_datetime, args.pattern)
end_datetime = datetime.datetime.strptime(args.end_datetime, args.pattern)

extract_batches_to_1_file(args.input_folder, start_datetime, end_datetime, args.output_folder)
print("Done.")
