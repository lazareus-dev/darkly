https://www.owasp.org/index.php/Testing_for_Cross_site_scripting
Since JavaScript is case sensitive, some people attempt to filter XSS by converting all characters to upper case, rendering Cross Site Scripting utilizing inline JavaScript useless. If this is the case, you may want to use VBScript since it is not a case sensitive language.

JavaScript:

<script>alert(document.cookie);</script>

Fix:
	escape the input
