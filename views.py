from django.http import HttpResponse

def index(request):
    return HttpResponse("""
<html>
	<head><title>Simple AWS Polls</title></head>
	<body>
		<h1><center>Simple AWS Polls</center></h1>
		<p><a href="/polls/">Polls</a></p>
		<p><a href="/admin/">Admin</a></p>
	</body>
</html>
""")

def status(request):
    return HttpResponse("""OK""")

