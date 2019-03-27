import application
from steps import create_cache_step
from azureml.pipeline.core import Pipeline
# from steps import vw_predict_step
from azureml.pipeline.core.graph import PipelineParameter


def create_pipeline(ws, ctx, parallel_jobs):
    cacheStep = create_cache_step.create_cache_step(
        workspace=ws,
        context=ctx
    )

    # predict_4 = vw_predict_step.vw_predict_step(
    #     workspace=ws,
    #     input_folder=cacheStep.output,
    #     commandline=PipelineParameter(
    #         name='extra_2',
    #         default_value='--cb_explore_adf --epsilon 0.2 --dsjson'
    #     ),
    #     name='NoMarginal'
    # )

    extractPipeline = Pipeline(workspace=ws, steps=[cacheStep])
    print ("extractPipeline is succesfully created.")

    extractPipeline.validate()
    print("extractPipeline is succesfully validated.")

    return extractPipeline
