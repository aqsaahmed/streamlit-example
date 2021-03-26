from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>Home | Recognition</title>
  <style>
	body {
	  counter-reset: my-sec-counter;
	}

	h7::before {
	  counter-increment: my-sec-counter 1;
	  content: counter(my-sec-counter);
	}
	</style>
	</head>

  <body>
  	<center>
    <h2 class="text-center mt-3">Please upload your report to get the predictions</h2>
    <form class="text-center" method="post" enctype="multipart/form-data">
    	{% csrf_token %}
    <div class="text-center">
	  <div class="form-group">
		    <label for="exampleFormControlFile1"><b><h4>Upload Report: </h4></b></label>
		    <input type="file" id="exampleFormControlFile1" name="img"><br>
		    <button type="submit" class="btn btn-primary mb-2">Upload</button>
	  </div>
	</div>
	</form>

	<table class="table table-dark">
	  <thead>
	    <tr>
	      <th scope="col">#</th>
	      <th scope="col">Characteristic</th>
	      <th scope="col">Value</th>
	    </tr>
	  </thead>
	  <tbody>
	  	{% for key,val in dictionary.items %}
		  <tr>
		  	<th scope="row"><h7></h7></th>
		    <td>{{ key }}</td>
		    <td>{{ val }}</td>
		  </tr>
	  	{% endfor %}
	  </tbody>
	</table>
</center>
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>
