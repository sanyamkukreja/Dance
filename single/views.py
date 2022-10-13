from django.shortcuts import render
from datetime import datetime

# Create your views here.
'''def dtl_learn(request):
    return render(request,'single/singleone.html',context={'a':10})
def dtl_learn(request):
    return render(request,'single/singleone.html',{'op':'pop'})
  dj=datetime.now()
    cname='django'
    duration='3 months'
    seats='12'
    intro='django is the best frameworP'
    a=24.67888
    pop={'name':cname,'time':duration,'avl':seats,'action':intro}
    return render(request,'single/singleone.html',pop,{'popo':dj,'p':a})''' 
def dtl_learn(request):
    student={'names':['snayam','gautam','vikas']}
    entry={
          'stu1':{'first':'sanyam'},
          'stu2':{'second':'vikas'},
    }
    
    return render(request,'sngle/singletwo.html',student,entry)