from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <title> coding </title>
    <body>
            <table border="2">
                    <caption> Top five Revenue Software Companies </caption>
                    <tr>
                                  <th> S.No </th>
                                  <td> 1 </td>
                                  <td> 2 </td>
                                  <td> 3 </td>
                                  <td> 4 </td>
                                  <td> 5 </td> 
                   </tr>
                   <tr>
                                  <th> company </th>
                                  <td> Microsoft </td>
                                  <td> Oracle </td>
                                  <td> IBM </td>
                                  <td> Sap </td>
                                  <td> Symaantec </td>
                   </tr>
                   <tr>               
                                 <th> Revenue </th>
                                 <td> 65 billuon </td>
                                 <td> 29.5 billion </td>
                                 <td> 29 billion </td>
                                 <td> 6.4 billion </td>
                                 <td> 7 billion </td>
                  </tr>
          </table>
     </body>
</html>
          
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()