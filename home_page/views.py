from django.shortcuts import render
from .models import welcome,links,about,education,projects,experience,skills,Contact_message
# Create your views here.
def home_page(request):
    if request.method == 'POST':
        print("post method")
        f_name = request.POST['firstname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        print("ended",f_name,email,subject,message)
        new_message = Contact_message(name = f_name,email = email, contact = subject, message = message)
        new_message.save()
        print("saved")
    welcome_obj = welcome.objects.all()
    abt_obj = about.objects.all()
    ln = links.objects.all()
    edu = education.objects.all()
    pro = projects.objects.all()
    exp = experience.objects.all()
    skill = skills.objects.all()
    skill_list = [skill[i:i + 4] for i in range(0, len(skill), 4)]
    return render(request,'index.html',{'resume':welcome_obj,'about':abt_obj,'links':ln,'edu':edu,'projects':pro,'experience':exp,'skills':skill_list})
