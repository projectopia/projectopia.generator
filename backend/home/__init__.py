home_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Welcome to Our API</title>
  <style>
    body {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      font-family: sans-serif;
      text-align: center;
      margin: auto;
      max-width: 600px;
      height: 100vh; /* Set the body height to full viewport height */
    }
    h1 {
      font-size: 40px;
      color: #333;
      margin-bottom: 20px;
    }
    p {
      font-size: 18px;
      line-height: 1.5;
      color: #666;
    }
    a {
      color: #007bff;
      text-decoration: none;
    }
    .button {
      background-color: #007bff;
      color: #fff;
      padding: 10px 20px;
      border-radius: 5px;
      text-decoration: none;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <h1>Welcome to Our API!</h1>
  <p>Explore our API documentation to discover its capabilities and start integrating it into your applications.</p>
  <p>Important note: Our API v1 endpoints use the prefix <code>/api/v1/&lt;route&gt;</code>.</p>
  <p>The API documentation is available at:</p>
  <a href="/docs" class="button">Visit API Documentation</a>
</body>
</html>
'''
