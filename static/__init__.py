default= '''
<html>
  <head>
   <link rel="stylesheet" type="text/css" href="mystyle.css">
   <script type="text/javascript" src="http://code.jquery.com/jquery-latest.min.js"></script>
  </head>
 <body style="background-color:#222222;">
  <div id='header'>
     <div id='title'>
      <h1>Martyni.co.uk</h1> 
     </div>
    <h2>Welcome</h2>
  </div>
  <div id='site'>
   <p>Please find this app of my internet speeds and latest bus times below</p>
   <script>
   console.log("Working");
   $("p").click($("p").append("<p> APPENDED</p>"););
   console.log("Working");
   </script>
   <p>This project has been built using <a href="http://dashing.io">Dashing<a>, <a href="https://mongodb.org">MongoDB</a>,<a href="http://bottlepy.org"> Bottle </a> and a <a href="https://www.raspberrypi.org">Raspberry Pi</a></p>
   
   <iframe name="iframe1" id="iframe1" src="http://192.237.193.16" frameborder="0" border="0" cellspacing="0" style="border-style: none;"></iframe>
  </div>
  <div id='footer'>
    <p><a href="mailto:martynjamespratt@gmail.com">Contact</a></p>
  </div>
 </body>
</html>
'''
