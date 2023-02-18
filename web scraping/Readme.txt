___________________________________________________________________            Web scraping in Python        _______________________________________________________________________________________________________ 
  
Web scraping is the process of using bots to extract content and data from a website. Unlike screen scraping, 
which only copies pixels displayed onscreen, web scraping extracts underlying HTML code and, with it, data stored 
in a database.

	Libraries = Python BeautifulSoup : a python package to scrap website   

	1.Setting up the Enviroment =

		libraries needed to download 

		.pip install requsts 
		.pip install html5lib 
		.pip install bs4 

	2. Fetching the HTML contents 

		. in order to work with the HTML we will have to get the HTML as a 
		string 
		.THe next step then will be to pars the HTML content and give it a 
		tree like structure so that it can be traversed!

	3. Parse the HTML 

		.Once the html is fetched using requests as an string we need to parse
		it 
		.for parsing we will use pythons's beautifulsoup module which will 
		creat a tree like structure for our DOM 

	4. HTML tree traversal 

		Once the HTML is fetched and parsed , the next step is to manipulate the tree 
		Susing BeautifulSoup's to get our job done 


	5. Important Links which i used to resolved BY codes Error:- 
		.https://stackoverflow.com/questions/63644025/always-getting-result-as-none-while-web-scraping-using-bs4

		 Error= Sorry, we just need to make sure you're not a robot. For best results, please make sure your browser is accepting cookies.
 
		first used amazon website to scrap data but It seems that Amazon blocks any crawling, I check it and when you run the code for the first time, 
		the content can be extracted. Whenever, the code is run immediately for the second time, it will be blocked. If you print out the soup variable, you will be faced the 
		above problem 
		.
		. 
Beautiful Soup Documentation

https://www.crummy.com/software/BeautifulSoup/bs4/doc/

   Copy right = AkarshanGhosh 