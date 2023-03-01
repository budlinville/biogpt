try:
    import os
    from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
    print("All imports ok ...")
except Exception as e:
    print("Error Imports : {} ".format(e))

# Config
default_max_length      = 60
default_num_answers     = 1
path_to_model           = '/mnt/efs1/models/biogpt'

# Create generator
model = AutoModelForCausalLM.from_pretrained(path_to_model)
tokenizer = AutoTokenizer.from_pretrained(path_to_model)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)


def format_http_response(status, result):
    is_error = status > 400

    body = { 'result': result } if not is_error else {
        'error': 'ERROR',
        'msg': result,
    }

    return {
        'statusCode': status,
        'body': body,
    }


def lambda_handler(event, _):
    print(event)
    if 'queryStringParameters' in event:
        params = event['queryStringParameters']
        if 'prompt' in params:
            prompt      = params['prompt']
            max_length  = default_max_length if 'max_length' not in params else int(params['max_length'])
            num_answers = default_num_answers if 'num_answers' not in params else int(params['num_answers'])

            print(prompt)
            print(max_length)
            print(num_answers)

            # Run the model
            result = generator(
                prompt,
                max_length = max_length,
                num_return_sequences = num_answers,
                do_sample = True
            )

            return format_http_response(200, [r['generated_text'] for r in result])
        
    return format_http_response(422, 'Missing field, "prompt"')
