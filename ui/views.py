from django.http import HttpResponse
from django.template import loader

def index(request):
    
	testlist = []
	testlist.append(["Test1", "Test2", "Test3"])
	testlist.append(["Test4", "Test5", "Test6"])
	testlist.append(["Test7", "Test8", "Test9"])
	template = loader.get_template('ui/index.html')
	context = { 'testlist': testlist }
	return HttpResponse(template.render(context, request))