from .forms import MessageForm

def message_form_processor(request):
    form = MessageForm()
    return {'footer_message_form': form}
