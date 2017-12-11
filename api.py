
print('Loading API-handler')

def get(event, context):

	print('Function: get')
	print(event)

	message = 'Hello %s, hope you are doing well.' % ('Michael')
	response = {
        'statusCode': 200,
        'body': message
    }

	return response