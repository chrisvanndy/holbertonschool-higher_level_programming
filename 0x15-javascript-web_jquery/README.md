# JQuery

### Import JQuery

```
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```

### Using elements, id's and classes

Define elemnents with a corresponding id in this way:

```
<div id="divTest"></div>
<script type="text/javascript">
$(function()
{
	$("#divTest").text("Test");
});
</script>
```

Elements with a specific class can be matched by writing a "." character followed by the name of the class.

```
<ul>
	<li class="bold">Test 1</li>
	<li>Test 2</li>
	<li class="bold">Test 3</li>
</ul>
<script type="text/javascript">
$(function()
{
	$(".bold").css("font-weight", "bold");
});
</script>
```

Similar to the above example, you can and should be as speicif as possible when matching elements.  Here is a re-written example using the "span" method:

```
$("span.bold").css("font-weight", "bold");
```

You can also match elemnts based on their tag names. For instance, you can match all links on a page in this way:

```
$("a")
```

Or you can match all div tags in this way:

```
$("div")
```


