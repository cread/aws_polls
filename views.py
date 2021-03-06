#   Copyright 2010 Chris Read <chris.read@gmail.com>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

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

