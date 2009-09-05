## Controlled Python Script "validate_gmap"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind state=state
##bind subpath=traverse_subpath
##parameters=api_key=''
##title=Validates an object title
##

if not api_key:
    state.setError('api_key', 'This field is required, please provide some information.', 'input_required')

if state.getErrors():
    return state.set(status='failure', portal_status_message='Please correct the indicated errors.')
else:
    return state

