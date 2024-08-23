from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt 


# Create your views here.
def accueil(request):
    return render(request, 'fao/accueil.html')

def analyse(request):
    return render(request, 'fao/analyse.html')

def echange(request):
    return render(request, 'fao/echange.html')

def chat(request):
  if request.method == 'POST':
    message = request.POST.get('name', '')
    response = 'ai response'
    #content1 = f'<div class="chat-message flex items-center justify-end"><p class="p-4 rounded-lg bg-blue-500 text-white">{message}</p></div>'
    #content2 = f'<div class="chat-message flex items-center"><p class="p-4 rounded-lg bg-gray-300">{response}</p></div>'
    #response_html = f"""
        #<div hx-swap-oob="innerHTML:#section1">{content1}</div>
        #<div hx-swap-oob="innerHTML:#section2">{content2}</div>
        #"""
    #return HttpResponse(response_html)

    return HttpResponse(f'<div class="chat-message flex items-center justify-end"><p class="p-4 rounded-lg bg-blue-500 text-white">{message}</p></div><div class="chat-message flex items-center"><p class="p-4 rounded-lg bg-gray-300">{response}</p></div>')
  return HttpResponse(status=400)



@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('dropzone-file')

        if uploaded_file:
            # with open('path/to/save/file', 'wb') as f:
            #     for chunk in uploaded_file.chunks():
            #         f.write(chunk)
            print(uploaded_file)
            data = f'<p>Fichier {uploaded_file} téléchargé avec succès!</p>'
            content1 = f'<p>reponse1</p>'
            content2 = f'<p>reponse2</p>'
            response_html = f"""
                <div hx-swap-oob="innerHTML:#upload-result">{data}</div>
                <div hx-swap-oob="innerHTML:#section1">{content1}</div>
                <div hx-swap-oob="innerHTML:#section2">{content2}</div>
                """
            return HttpResponse(response_html)
            #return HttpResponse(data)
        else:
            return HttpResponse('Aucun fichier n\'a été sélectionné.')
    else:
        return HttpResponseBadRequest()
    

def analyse_action(request):
    selected_value = request.GET.get('hs-select-label')
    print(selected_value)

    if selected_value == "1":
        section1_content = '<h1 class="mt-4">1Updated Capture for Option 1</h1><img src="https://example.com/image1.jpg" alt="" class="p-4 h-[750px] w-[100%]">'
        section2_content = '<h1 class="mt-4">1Updated Description for Option 1</h1><h1 class="mt-20">Updated Solution for Option 1</h1>'
    elif selected_value == "2":
        section1_content = '<h1 class="mt-4">2Updated Capture for Option 2</h1><img src="https://storage.needpix.com/rsynced_images/document-872506_1280.jpg" alt="" class="p-4 h-[750px] w-[100%]">'
        section2_content = '<h1 class="mt-4">2Updated Description for Option 2</h1><h1 class="mt-20">Updated Solution for Option 2</h1>'
    elif selected_value == "3":
        section1_content = '<h1 class="mt-4">3Updated Capture for Option 3</h1><img src="https://example.com/image3.jpg" alt="" class="p-4 h-[750px] w-[100%]">'
        section2_content = '<h1 class="mt-4">3Updated Description for Option 3</h1><h1 class="mt-20">Updated Solution for Option 3</h1>'
    else:
        section1_content = '<h1 class="mt-4">4Default Capture</h1>'
        section2_content = '<h1 class="mt-4">4Default Description</h1><h1 class="mt-20">Default Solution</h1>'

    response_html = f"""
        <div hx-swap-oob="innerHTML:#section1">{section1_content}</div>
        <div hx-swap-oob="innerHTML:#section2">{section2_content}</div>
        """
    return HttpResponse(response_html)

