with open('e:/intern/django/hostpital/app/views.py', 'r') as f:
    c = f.read()

import re
new_c = re.sub(
    r'def doc\(request\):.*?return render\(request,\'index\.html\'\)',
    '''def doc(request):
    if request.method=='POST':
        n=request.POST['doctor_name']
        s=request.POST['specialization']
        p=request.POST.get('password')

        if User.objects.filter(username=n).exists():
            return HttpResponse("A doctor with this name already exists. Please choose a different name.")
        
        user = User.objects.create_user(username=n, password=p)
        data=Doctor(user=user, doctor_name=n, specialization=s)
        data.save()
        return render(request,'index.html',{'key':Doctor.objects.all()})
    return render(request,'index.html', {'key': Doctor.objects.all()})''',
    c,
    flags=re.DOTALL
)

with open('e:/intern/django/hostpital/app/views.py', 'w') as f:
    f.write(new_c)
