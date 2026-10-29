"""Terjemahan Inggris untuk materi (urutannya sejajar dengan content/lessons.py, quizzes.py, reference.py, pages.py)."""

# ---------------------------------------------------------------- pelajaran: (judul, isi)
LESSONS_EN = {
"html": [
 ("Introduction to HTML",
  "HTML (HyperText Markup Language) is the markup language that gives a web page its structure. The browser reads tags such as <h1> and <p> and displays them as headings and paragraphs.\n\nEvery HTML document starts with <!DOCTYPE html> and contains <head> for page information and <body> for the visible content."),
 ("Elements, Attributes, and Links",
  "An element consists of an opening tag, content, and a closing tag. Attributes give extra information about an element, such as href on a link or src and alt on an image.\n\nAlways fill in the alt attribute on images so the page is understandable to screen readers and still meaningful if the image fails to load."),
 ("Lists and Tables",
  "Use <ul> for bulleted lists, <ol> for numbered lists, and <li> for each item. Data in rows and columns is built with <table>, <tr> (row), <th> (column heading), and <td> (cell)."),
 ("Forms",
  "Forms collect user input. The <input> element has many types (text, email, password, number), and <label> explains each field. The required attribute makes the browser validate mandatory fields."),
],
"css": [
 ("Introduction to CSS and Selectors",
  "CSS (Cascading Style Sheets) controls how HTML elements look. A CSS rule consists of a selector (what to change) and a declaration block (property: value).\n\nCommon selectors: element name (p), class (.card), and id (#header)."),
 ("Colors and the Box Model",
  "Every element is a layered box: content, padding (inner space), border, and margin (outer space). Understanding the box model helps you control spacing and size precisely.\n\nUse box-sizing: border-box so an element's width already includes its padding and border."),
 ("Layout with Flexbox",
  "Flexbox arranges elements in a row or column with ease. Set display: flex on the container, then control direction (flex-direction), alignment (justify-content, align-items), and spacing (gap)."),
 ("Responsive Design with Media Queries",
  "Media queries apply CSS rules only under certain conditions, such as screen width. In the mobile-first approach, write base styles for phones, then add rules for wider screens."),
],
"javascript": [
 ("Variables and Data Types",
  "JavaScript makes web pages interactive. Use const for values that never change and let for those that do; avoid var. Basic types: string, number, boolean, null, undefined."),
 ("Functions",
  "Functions wrap steps so they can be reused. Arrow functions are a short syntax that is very common in modern JavaScript."),
 ("Arrays and Loops",
  "An array stores many values in order. Methods such as map, filter, and reduce process arrays without writing manual loops."),
 ("The DOM and Events",
  "The DOM is a representation of the HTML page that JavaScript can change. Select elements with querySelector, then attach event listeners to respond to clicks, input, and more."),
],
"python": [
 ("Hello Python: Variables and Input/Output",
  "Python is known for its clean syntax. Variables are created directly with =, without type declarations. Use print() to display output and input() to read user input."),
 ("Conditionals and Loops",
  "if/elif/else chooses a program path based on conditions. for repeats over a sequence of data, while repeats as long as a condition is true. Mind the indentation: it marks the code block."),
 ("Lists and Dictionaries",
  "A list stores ordered data that can be changed; a dict stores key-value pairs. Both are the most frequently used data structures in Python."),
 ("Functions and Modularity",
  "Functions split a program into small parts, each with one job. Use return to give back a result and choose names that explain what the function does. Modular programs are easier to read, test, and extend."),
],
"sql": [
 ("SELECT: Reading Data",
  "SQL (Structured Query Language) is used to manage data in relational databases. SELECT chooses columns from a table; the * sign means all columns."),
 ("WHERE, ORDER BY, LIMIT",
  "WHERE filters rows, ORDER BY sorts results (ASC ascending, DESC descending), and LIMIT restricts how many rows are shown."),
 ("INSERT, UPDATE, DELETE",
  "Three commands change data: INSERT adds rows, UPDATE modifies them, and DELETE removes them. Always include WHERE on UPDATE and DELETE so you do not change the whole table."),
 ("JOIN: Combining Tables",
  "JOIN combines rows from two tables based on related columns, usually a foreign key. INNER JOIN returns only the rows that match in both tables."),
],
"java": [
 ("Java Program Structure",
  "A Java program lives inside a class. Execution starts from the main method. Java is an object-oriented language that is compiled to bytecode and run on the JVM."),
 ("Variables and Data Types",
  "Java is statically typed: a variable's type must be declared. Common primitive types: int, double, boolean, char. String is a class for text."),
 ("Classes and Objects",
  "A class is a blueprint; an object is built from it. A class contains attributes (data) and methods (behavior). The keyword new creates an object."),
 ("Arrays and Loops",
  "An array stores a fixed number of values of the same type. A for or for-each loop is used to walk through it."),
],
"php": [
 ("PHP Basic Syntax",
  "PHP runs on the server and produces HTML. PHP code sits inside <?php ... ?> tags. Each statement ends with a semicolon, and variables start with a $ sign."),
 ("Arrays and Loops",
  "PHP has indexed arrays and associative arrays (key-value). foreach walks through an array concisely."),
 ("Functions",
  "Functions are created with the function keyword. Parameter and return types can be declared to make code clearer and safer."),
 ("Handling Form Data",
  "Form data arrives through the superglobals $_POST or $_GET. Always validate and clean input before using it; use htmlspecialchars() when displaying it again to prevent XSS."),
],
"c": [
 ("Your First C Program",
  "C is a foundational language close to the hardware. A program starts from the main() function. The stdio.h header provides printf and scanf for input and output."),
 ("Variables and Input",
  "C is statically typed: int for whole numbers, float/double for decimals, char for characters. scanf reads input; use %d for int and %f for float. Note the & sign in scanf."),
 ("Loops and Conditionals",
  "for, while, and do-while repeat code; if/else if/else handles branching. The example below prints the even numbers from 1 to 10."),
 ("Arrays and Basic Pointers",
  "An array stores data of the same type. A pointer stores a memory address; the & operator takes an address and * accesses the value at that address. Pointers are the key to understanding memory in C."),
],
"cpp": [
 ("Your First C++ Program",
  "C++ extends C with object-oriented programming and the standard library (STL). cout prints output and cin reads input from the iostream library."),
 ("Vectors and Strings",
  "std::vector is a dynamic array whose size can change, and std::string handles text safely. Both are far more convenient than C-style arrays and char[]."),
 ("Classes and Objects",
  "A class bundles data and behavior. A constructor initializes the object, while private/public modifiers control access to class members."),
 ("STL Algorithms",
  "The algorithm header provides ready-made functions such as sort, find, and count. Using them saves time and reduces bugs compared with rewriting them."),
],
"csharp": [
 ("Your First C# Program",
  "C# is a modern language from Microsoft for .NET, desktop and web apps, and Unity games. Console.WriteLine prints text to the console."),
 ("Variables and Data Types",
  "C# is statically typed but supports var for type inference. Common types: int, double, bool, string. String interpolation uses the $ prefix."),
 ("Lists and LINQ",
  "List<T> is a dynamic collection. LINQ lets you filter and process collections with concise syntax, similar to SQL."),
 ("Classes and Properties",
  "C# classes use properties (get/set) to access data in a controlled way. A constructor prepares the object when it is created."),
],
"react": [
 ("Components",
  "React builds interfaces from components: functions that return JSX (HTML inside JavaScript). Component names must start with a capital letter."),
 ("Props",
  "Props are data passed from a parent component to a child, like HTML attributes. Props are read-only inside the receiving component."),
 ("State with useState",
  "State stores data that changes and triggers a re-render when it does. The useState hook returns the current value and a function to change it."),
 ("Rendering Lists and Conditions",
  "Use map to render lists and give each item a unique key property. Conditional rendering uses the ternary operator or &&."),
],
"mysql": [
 ("Creating Databases and Tables",
  "MySQL is a relational database management system. A database is created with CREATE DATABASE, and the data structure is defined with CREATE TABLE together with each column's type."),
 ("Data Types and Keys",
  "Choose the most suitable data type: INT for whole numbers, VARCHAR(n) for short text, DATE for dates, DECIMAL for precise numbers. A PRIMARY KEY identifies a row uniquely, and a FOREIGN KEY links tables."),
 ("Aggregation with GROUP BY",
  "Aggregate functions (COUNT, SUM, AVG, MIN, MAX) summarize many rows. GROUP BY groups rows, and HAVING filters the groups."),
 ("Indexes and EXPLAIN",
  "An index speeds up searches on frequently filtered columns, at the cost of space and write speed. EXPLAIN shows how MySQL executes a query so you can optimize it."),
],
}

# ---------------------------------------------------------------- quiz: (pertanyaan, [opsi], penjelasan); opsi yang sama dibiarkan
QUIZ_EN = {
"html": [
 ("The abbreviation HTML stands for...", None, "HTML = HyperText Markup Language."),
 ("Which tag is correct for the largest heading?", None, "<h1> is the highest-level heading."),
 ("Which attribute gives alternative text to an image?", None, "alt is read by screen readers and shown when the image fails to load."),
 ("Which element creates a numbered list?", None, "<ol> = ordered list; <ul> is bulleted."),
],
"css": [
 ("CSS is used to...", ["Control page appearance", "Store data", "Create a database", "Run servers"], "CSS controls how HTML elements look."),
 ("Selector for a class named kartu?", None, "A class uses a dot, an id uses #."),
 ("Which property sets the space INSIDE an element's border?", None, "padding = inner space; margin = outer space."),
 ("Which display value gives a flexible layout?", None, "display: flex enables Flexbox."),
],
"javascript": [
 ("Which keyword declares a constant that cannot be reassigned?", None, "const prevents the variable from being reassigned."),
 ("What is the result of typeof \"halo\"?", None, "typeof \"halo\" returns \"string\"."),
 ("Which array method filters elements?", None, "filter returns the elements that satisfy the condition."),
 ("How do you select the element with id=\"judul\"?", None, "querySelector uses CSS selectors; an id starts with #."),
],
"python": [
 ("What is the output of print(2 ** 3)?", None, "** is the power operator: 2 to the power of 3 = 8."),
 ("Which data structure holds key-value pairs?", None, "A dict stores keys and values."),
 ("Which keyword defines a function?", ["func", "def", "function", "lambda only"], "Functions are defined with def."),
 ("What is the result of len([1, 2, 3, 4])?", None, "len counts the elements: 4."),
],
"sql": [
 ("Which command reads data?", None, "SELECT chooses data from a table."),
 ("Which clause filters rows?", ["FILTER", "HAVING only", "WHERE", "ORDER BY"], "WHERE filters rows before they are grouped."),
 ("Sort from largest to smallest?", None, "DESC = descending."),
 ("JOIN is used to...", ["Delete a table", "Combine rows from two tables", "Create an index", "Copy a database"], "JOIN combines tables based on related columns."),
],
"java": [
 ("The entry point of a Java program?", None, "Execution starts from public static void main."),
 ("Which data type is used for text?", ["char[] only", "String", "text", "Str"], "String is a class for text."),
 ("Which keyword creates an object?", None, "new ClassName() creates an object."),
 ("Java runs on...", ["The JVM", "The CLR", "A Python interpreter", "The browser"], "Java bytecode is run by the Java Virtual Machine."),
],
"php": [
 ("A PHP variable starts with...", None, "Example: $nama."),
 ("Which statement displays text?", None, "echo prints output."),
 ("Which superglobal holds POST form data?", None, "$_POST contains POST form data."),
 ("Which function prevents XSS when displaying input?", None, "htmlspecialchars converts special HTML characters."),
],
"c": [
 ("Which function prints to the screen in C?", None, "printf from stdio.h."),
 ("Which printf format is for integers?", None, "%d = int; %f = float; %s = string; %c = char."),
 ("Which operator takes a variable's address?", None, "& takes the address; * accesses the value of a pointer."),
 ("The first index of an array in C?", ["0", "1", "-1", "It depends"], "Array indexes start at 0."),
],
"cpp": [
 ("The standard output object in C++?", None, "cout from <iostream>."),
 ("Dynamic array in the STL?", ["vector", "stack only", "map", "pair"], "std::vector can change its size."),
 ("STL function for sorting?", None, "sort(begin, end) from <algorithm>."),
 ("Which modifier makes a member accessible only inside the class?", None, "private restricts access to inside the class."),
],
"csharp": [
 ("Command to print text to the console?", None, "Console.WriteLine from the System namespace."),
 ("What is var for in C#?", ["Dynamic typing", "Compile-time type inference", "A global variable", "A constant"], "var lets the compiler infer the type; it is still statically typed."),
 ("LINQ is used to...", ["Draw the UI", "Process and filter collections", "Run SQL Server", "Create classes"], "LINQ = Language Integrated Query."),
 ("Syntax for an auto-property?", None, "Example: public string Nama { get; set; }."),
],
"react": [
 ("A React component must start with a ... letter", ["Capital", "Lowercase", "Number", "Underscore"], "A capital letter distinguishes it from a normal HTML tag."),
 ("Which hook stores local state?", None, "useState returns [value, setter]."),
 ("Data passed from parent to child is called...", None, "Props are read-only."),
 ("Which property is required when rendering a list with map?", None, "key helps React track list items."),
],
"mysql": [
 ("Command to create a new table?", None, "CREATE TABLE name (...)."),
 ("Attribute for an auto-increasing value?", None, "AUTO_INCREMENT is commonly used on primary keys."),
 ("Aggregate function to count rows?", None, "COUNT(*) counts rows."),
 ("How do you see a query's execution plan?", None, "EXPLAIN SELECT ... shows the execution plan."),
],
}

# ---------------------------------------------------------------- cheat sheet: deskripsi saja (sejajar dengan content/reference.py)
REF_EN = {
"html": ["Nested headings; h1 is the most important", "Text paragraph", "Link to another page", "Display an image with alternative text",
         "Bulleted / numbered lists and their items", "Table, rows, and cells", "Form and input fields", "Generic block / inline container",
         "Semantic elements that structure a page"],
"css": ["Basic form of a CSS rule", "Text and background color", "Outer space, inner space, border", "One-dimensional flexible layout",
        "Two-dimensional layout (rows and columns)", "Rules for specific screen widths", "Class and id selectors", "Font family and size",
        "Style when the cursor is over an element"],
"javascript": ["Declare constants and variables", "Function declaration", "Arrow function", "Process arrays functionally", "Select a DOM element",
               "Attach an event handler", "Fetch data from the network", "Convert JSON <-> object", "Template literal"],
"python": ["Display a value", "Read text input", "Conditional branching", "Loop n times", "Conditional loop", "list and dict", "Define a function",
           "Frequently used built-in functions", "Handle errors", "Open a file safely"],
"sql": ["Read data", "Filter rows", "Sort results", "Add a row", "Modify rows", "Delete rows", "Combine tables", "Group rows and filter groups", "Aggregate functions"],
"java": ["Program entry point", "Print to the console", "Common data types", "Conditional branching", "For loop", "Define a class", "Create an object",
         "Dynamic list", "Exception handling"],
"php": ["PHP code block", "Variables start with $", "Display output", "Associative array", "Iterate over an array", "Define a function",
        "Form / URL data", "Prevent XSS when displaying input", "Include another file"],
"c": ["Include the I/O library", "Program entry point", "Print with a format", "Read input", "Conditional branching", "Loops", "Fixed-size array",
      "Pointer to the address of x", "Dynamic memory allocation and release"],
"cpp": ["Input/output library", "Print output", "Read input", "Dynamic array", "Text type", "Define a class", "Sort (STL)", "Range-based for",
        "Smart pointer (freed automatically)"],
"csharp": ["Print to the console", "Declaration with type inference", "Common data types", "Conditional branching", "Iterate over a collection", "Dynamic list",
           "Filtering with LINQ", "Class with a property", "Exception handling"],
"react": ["Function component", "Pass props", "Local state", "Side effects after render", "Render a list", "Conditional rendering", "Event handling", "Export a component"],
"mysql": ["Create a database", "Create a table", "Common data types", "Primary key and foreign key", "Auto-increasing value", "Create an index",
          "View a query's execution plan", "View the list of tables and their structure", "Paginate results"],
}

# ---------------------------------------------------------------- katalog bahasa
TAGLINE_EN = {
    "html": "The skeleton and structure of web pages.", "css": "Colors, layout, and the look of pages.", "javascript": "Make web pages interactive.",
    "python": "A versatile language: web, data, AI, automation.", "sql": "The standard language for managing databases.",
    "java": "An object-oriented language for large-scale applications.", "php": "A server-side language for building dynamic sites.",
    "c": "The foundation of systems programming and memory.", "cpp": "C with OOP and a rich standard library.",
    "csharp": "A modern language for .NET, games (Unity), and desktop.", "react": "A component-based UI library built on JavaScript.",
    "mysql": "The most popular relational database system.",
}
DOCS_NAME_EN = {"Dokumentasi Python": "Python Documentation"}

# ---------------------------------------------------------------- modul bawaan: (judul, deskripsi) sejajar dengan SEED_MODULES
SEED_EN = [
    ("Introduction to HTML", "Basic web page structure and main tags."), ("CSS Basics", "Selectors, colors, and simple layout."),
    ("Python Variables and Data Types", "Learn variables, data types, and operators."), ("Python Conditionals and Loops", "if/elif/else, for, and while."),
    ("Python Functions and Modularity", "Splitting a program into structured functions."), ("Interactive JavaScript", "The DOM and events on web pages."),
    ("Basic SQL Queries", "SELECT, WHERE, and ORDER BY."), ("MySQL Database Design", "Normalization and relationships between tables."),
]

# ---------------------------------------------------------------- roadmap: (judul, deskripsi, [catatan langkah]) sejajar dengan ROADMAP
ROADMAP_EN = [
    ("Front-End Developer", "Build interactive and responsive web interfaces.",
     ["Start with page structure.", "Make it beautiful and responsive.", "Add interactivity.", "Build component-based UIs."]),
    ("Back-End Developer", "Create server logic and store data.",
     ["Master programming fundamentals.", "Manage data with queries.", "Build dynamic server-side sites.", "Design efficient databases."]),
    ("Software Engineer", "Understand computer fundamentals and large-scale applications.",
     ["Understand memory and pointers.", "Add OOP and the STL.", "Build object-oriented applications.", "Explore .NET and Unity games."]),
    ("Data and Automation", "Process data and automate work.",
     ["The main language for data and AI.", "Retrieve and summarize data.", "Manage relational databases."]),
]

# ---------------------------------------------------------------- halaman info: (judul, [(judul bagian, isi)]) sejajar dengan INFO
INFO_EN = {
    "tentang": ("About UG-Stack", [
        ("What is UG-Stack?", "UG-Stack is a Python (Flet) programming learning platform that runs on the web and Android. The lessons, cheat sheets, and quizzes are written in-house, then enriched automatically with content from trusted sources."),
        ("Automatic content sources", "Wikipedia (summaries), MDN Web Docs (web references), Stack Overflow (top questions), DEV Community (community articles), and GitHub (popular repositories). Everything is fetched through public APIs, always links back to the original source, and is cached for 24 hours so it still opens offline."),
        ("Content licenses", "Text from Wikipedia, MDN, and Stack Overflow is CC BY-SA licensed and belongs to its original authors. UG-Stack only shows summaries and links, not full copies of articles."),
    ]),
    "komunitas": ("Community and Contact", [
        ("Join in", "Follow UG-Stack updates, ask questions, and share projects with fellow learners. Official community links can be added by the maintainer in content/pages.py."),
        ("Need help?", "Start from the Roadmap or Tutorial page. For specific questions, use the Search feature: it shows related questions from Stack Overflow."),
    ]),
    "aplikasi": ("Install the UG-Stack App", [
        ("Web", "Run python main.py and open http://127.0.0.1:8550 in your browser. The layout adapts automatically to the screen width."),
        ("Android (APK)", "Install the Flutter SDK, JDK 17, and the Android SDK, then run flet build apk in the project folder. Copy the .apk file from build/apk to your phone and install it. Details are in the README."),
        ("Data in the app", "On the APK, user data and the content cache are stored in the device storage so they remain after the app is closed."),
    ]),
    "spaces": ("UG-Stack Spaces", [
        ("A space for code experiments", "Use the Try it Editor to try code examples from each lesson. Open a lesson, then press the Try it Yourself button to load the code into the editor."),
        ("Coming soon", "Saving personal projects and sharing code result links."),
    ]),
}

# ---------------------------------------------------------------- soal tambahan (urutan sejajar dengan content/quizzes.py)
QUIZ_EN["html"].extend([
 ("Which element creates a link?", None, "<a> with the href attribute creates a link."),
 ("Which is the correct closing tag for a paragraph?", None, "Every <p> is closed with </p>."),
 ("Which attribute makes a form field mandatory?", None, "The required attribute makes the browser validate the field."),
 ("Which semantic element marks the main navigation?", None, "<nav> marks a group of navigation links."),
])
QUIZ_EN["css"].extend([
 ("Which property changes text color?", None, "The color property sets text color."),
 ("Which unit is relative to the screen width?", None, "vw = 1% of the viewport width."),
 ("Which flex setting centers items along the main axis?", None, "justify-content controls alignment on the main axis."),
 ("Which selector applies while the cursor is over a button?", None, ":hover applies while the cursor is over an element."),
])
QUIZ_EN["javascript"].extend([
 ("What is the result of 2 + \"2\" in JavaScript?", None, "The + operator concatenates strings, so the result is \"22\"."),
 ("How do you change an element's text?", None, "textContent changes the element's text."),
 ("Which array method adds an element at the end?", None, "push adds an element to the end of the array."),
 ("Which operator compares value and type?", None, "=== compares both value and type."),
])
QUIZ_EN["python"].extend([
 ("How do you write a single-line comment in Python?", None, "Comments start with #."),
 ("What is the result of 7 // 2?", None, "// is floor division: 7 // 2 = 3."),
 ("Which keyword handles errors?", None, "try ... except catches errors."),
 ("Which data type is immutable?", None, "A tuple cannot be changed after it is created."),
])
QUIZ_EN["sql"].extend([
 ("Which aggregate function gives the average?", None, "AVG computes the average."),
 ("Which clause groups rows?", None, "GROUP BY groups rows."),
 ("Which command deletes specific rows?", None, "DELETE FROM ... WHERE removes rows."),
 ("Which key links two tables?", None, "A foreign key references another table's primary key."),
])
QUIZ_EN["java"].extend([
 ("Which data type stores decimal numbers?", None, "double stores decimal numbers."),
 ("Which collection has a dynamic size?", None, "An ArrayList can change its size."),
 ("Which keyword is used for inheritance?", None, "extends creates a subclass."),
 ("Which method runs automatically when an object is created?", ["Destructor", "Constructor", "main", "finalize"], "The constructor initializes a new object."),
])
QUIZ_EN["php"].extend([
 ("Which operator concatenates strings in PHP?", None, "The dot (.) concatenates strings."),
 ("Which function counts array elements?", None, "count() counts array elements."),
 ("Which superglobal holds data from the URL?", None, "$_GET holds URL parameters."),
 ("How do you include another file?", None, "include brings in another PHP file."),
])
QUIZ_EN["c"].extend([
 ("Which type stores a single character?", None, "char stores one character."),
 ("Which function allocates dynamic memory?", None, "malloc allocates memory on the heap."),
 ("What is the result of 10 % 3?", None, "% is the remainder: 10 % 3 = 1."),
 ("What marks the end of a C string?", None, "A string ends with the null character '\\0'."),
])
QUIZ_EN["cpp"].extend([
 ("Which operator creates an object on the heap?", None, "new allocates a dynamic object."),
 ("Which symbol declares a reference (alias) to a variable?", None, "int &r = x; creates a reference (alias)."),
 ("Which container stores key-value pairs?", None, "std::map stores key-value pairs."),
 ("How do you write public inheritance?", None, "Inheritance uses a colon and an access specifier."),
])
QUIZ_EN["csharp"].extend([
 ("How do you create a list of strings?", None, "List<T> is a generic list."),
 ("Which keyword declares a constant?", None, "const declares a constant."),
 ("The ?. operator is used for...", ["Safe null checking", "Loops", "Division", "String comparison"], "The null-conditional operator avoids NullReferenceException."),
 ("Which statement handles exceptions?", None, "try/catch handles exceptions."),
])
QUIZ_EN["react"].extend([
 ("Which hook handles side effects such as loading data?", None, "useEffect runs after render."),
 ("Which JSX syntax displays the variable nama?", None, "Curly braces embed JavaScript expressions."),
 ("How is the CSS class attribute written in JSX?", None, "JSX uses className."),
 ("State should be changed with...", ["The setter function from useState", "Mutating the variable directly", "document.getElementById", "window.state"], "Use the setter so React re-renders."),
])
QUIZ_EN["mysql"].extend([
 ("Which command adds a column to a table?", None, "ALTER TABLE ... ADD COLUMN adds a column."),
 ("Which data type stores a date?", None, "DATE stores a date."),
 ("Which clause limits the number of rows?", None, "LIMIT n limits the number of rows."),
 ("Which function joins text?", None, "CONCAT joins strings."),
])

# ---- 20_SOAL_EN_PER_BAHASA
QUIZ_EN["html"].extend([
 ('Which tag inserts a single line break without starting a new paragraph?', None, '<br> produces a single line break.'),
 ('Which attribute on <a> opens the link in a new tab?', None, 'target="_blank" opens the link in a new tab.'),
 ('Which HTML5 semantic element represents the page footer?', None, '<footer> is the semantic element for the bottom section.'),
 ('Which tag creates a bulleted (unordered) list?', None, '<ul> creates an unordered list.'),
 ('Which tag defines a header cell in an HTML table?', None, '<th> defines a table header cell.'),
 ('Which input type displays a date picker in an HTML form?', None, '<input type="date"> shows a date picker.'),
 ('Which element wraps document metadata such as <title> and <meta>?', None, '<head> holds document metadata.'),
 ('Which attribute merges two columns in a table cell?', None, 'colspan spans a cell across multiple columns.'),
 ('Which HTML tag marks bold text with strong importance?', None, '<strong> marks important text and renders it in bold.'),
 ('Which element creates a drop-down selection list?', None, '<select> together with <option> builds a drop-down menu.'),
 ('Which attribute shows a short hint inside an input field?', None, 'placeholder displays a hint inside an empty input field.'),
 ('Which declaration at the very top marks an HTML5 document?', None, '<!DOCTYPE html> enables standard HTML5 mode.'),
])
QUIZ_EN["css"].extend([
 ('Which property changes the typeface (font) of text?', None, 'font-family sets the font family of text.'),
 ('Which property makes the corners of a box rounded?', None, 'border-radius controls corner rounding.'),
 ('Which position value keeps an element pinned to the screen while scrolling?', None, 'position: fixed keeps an element fixed to the viewport.'),
 ("Which property sets the space OUTSIDE an element's border?", None, 'margin sets the outer space around a border.'),
 ('Which property removes the underline from an <a> link?', None, 'text-decoration: none removes the link underline.'),
 ('Which property sets the size of text?', None, 'font-size controls the size of letters.'),
 ('Which display value hides an element completely from the layout?', None, 'display: none hides the element without taking up space.'),
 ('Which Flexbox property changes the direction to vertical (column)?', None, 'flex-direction: column arranges items top to bottom.'),
 ('Which property controls the transparency level of an element?', None, 'opacity ranges from 0 to 1.'),
 ("Which property adds a shadow effect to an element's box?", None, 'box-shadow adds a shadow around a box.'),
 ('Which CSS selector selects every element on the page?', None, 'The universal selector * targets all elements.'),
 ('Which property sets the stacking order of overlapping elements?', None, 'z-index controls the stack order.'),
])
QUIZ_EN["javascript"].extend([
 ('Which method converts a JSON string into a JavaScript object?', None, 'JSON.parse() parses a JSON string into an object.'),
 ('Which keyword declares an asynchronous function?', None, 'async is placed before function.'),
 ('Which array method creates a new array by calling a function on every element?', None, 'map() transforms each element into a new value.'),
 ('Which property returns the number of elements in an array?', None, 'arr.length returns the array length.'),
 ('Which function runs code once after a specified delay?', None, 'setTimeout(fn, ms) delays function execution.'),
 ('Which operator provides a fallback value when the left side is null or undefined?', None, 'The nullish coalescing operator (??) checks for null/undefined.'),
 ('Which method removes the LAST element from an array?', None, 'pop() removes and returns the last element.'),
 ('How do you write a template literal that supports variable interpolation?', None, 'Template literals use backticks (` `).'),
 ('Which method prints a message to the browser console?', None, 'console.log() outputs messages to the console.'),
 ('What is the boolean value of Boolean(0) in JavaScript?', None, 'The number 0 is falsy, so it evaluates to false.'),
 ('Which string method converts all letters to uppercase?', None, 'str.toUpperCase() converts characters to uppercase.'),
 ('Which event is fired when a form is submitted?', None, 'The submit event fires when a form is sent.'),
])
QUIZ_EN["python"].extend([
 ('Which list method adds a single element to the very end?', None, 'list.append(x) adds an item to the end of a list.'),
 ('What is the result of [x * 2 for x in [1, 2, 3]]?', None, 'The list comprehension multiplies each item by 2.'),
 ('Which dictionary method safely retrieves a value without raising KeyError?', None, 'd.get(k) returns None when the key is missing.'),
 ('Which keyword imports a library or module in Python?', None, 'import is used to load a module.'),
 ("What is the result of 'python'.upper()?", None, 'upper() converts all characters to uppercase.'),
 ('Which built-in function generates a sequence of integers?', None, 'range(start, stop) generates a sequence of integers.'),
 ('Which operator checks whether a value exists inside a list?', None, 'The in operator checks membership.'),
 ('Which Python data structure stores only unique elements (no duplicates)?', None, 'A set stores unique elements.'),
 ('What value does a Python function return if it has no return statement?', None, 'Without return, a function returns None.'),
 ('What is the recommended way to open a file so it closes automatically?', None, 'A with block closes the file automatically.'),
 ('What is the result of [10, 20, 30][-1]?', None, 'Index -1 accesses the last element.'),
 ('Which built-in function sorts an iterable and returns a new list?', None, 'sorted(iterable) returns a new sorted list.'),
])
QUIZ_EN["sql"].extend([
 ('Which command inserts a new row into a table?', None, 'INSERT INTO table_name (...) VALUES (...) adds a row.'),
 ('Which command modifies column values in existing rows?', None, 'UPDATE table_name SET column = value WHERE ...'),
 ('Which clause filters grouped results after GROUP BY?', None, 'HAVING filters aggregated groups.'),
 ('Which keyword removes duplicate rows from a SELECT result?', None, 'SELECT DISTINCT returns only unique values.'),
 ("Which operator in WHERE matches a text pattern (e.g. 'A%')?", None, 'LIKE is used with % and _ wildcards.'),
 ('Which aggregate function finds the largest value in a column?', None, 'MAX(column) returns the maximum value.'),
 ('Which aggregate function adds up all numeric values in a column?', None, 'SUM(column) computes the total sum.'),
 ('Which condition correctly checks whether a column is NULL?', None, 'Use IS NULL or IS NOT NULL in SQL.'),
 ('Which JOIN returns all rows from the left table?', None, 'LEFT JOIN keeps all rows from the left table.'),
 ('Which command completely removes a table from the database?', None, 'DROP TABLE deletes the table and its structure.'),
 ('Which operator selects values within an inclusive range?', None, 'BETWEEN a AND b checks values from a through b.'),
 ('Which keyword gives a column or table an alias name?', None, 'SELECT column AS alias_name FROM table.'),
])
QUIZ_EN["java"].extend([
 ('Which keyword declares a constant in Java?', None, 'final prevents a variable from being reassigned.'),
 ('Which keyword implements an interface in a class?', None, 'class A implements B fulfills an interface contract.'),
 ('Which method returns the character length of a String object?', None, 'String has a length() method.'),
 ('What is the correct way to compare the contents of two Strings in Java?', None, 'equals() compares character content.'),
 ('Which block always runs after try/catch?', None, 'The finally block always executes.'),
 ('Which keyword refers to the current object inside a class method?', None, 'this refers to the current object instance.'),
 ('Which primitive type stores true or false in Java?', None, 'Java uses the boolean keyword.'),
 ('Which standard package must be imported to use ArrayList?', None, 'ArrayList lives in the java.util package.'),
 ('Which modifier lets a method be called on the class name directly?', None, 'A static method belongs to the class itself.'),
 ('Which keyword calls a constructor or method of the parent class?', None, 'super refers to the superclass.'),
 ('Which 64-bit integer type is used in Java?', None, 'long is 64-bit.'),
 ('What is the file extension of compiled Java bytecode?', None, 'javac produces .class bytecode files.'),
])
QUIZ_EN["php"].extend([
 ('Which function checks whether a variable is set and not null?', None, 'isset($var) returns true if set and not null.'),
 ('Which function converts an array into a JSON string in PHP?', None, 'json_encode() produces a JSON string.'),
 ('Which superglobal stores user session data across pages?', None, '$_SESSION stores server-side session state.'),
 ('Which function must be called before using $_SESSION?', None, 'session_start() starts or resumes a session.'),
 ('Which function removes whitespace from both ends of a string?', None, 'trim($str) strips whitespace from both ends.'),
 ('Which function converts a JSON string into an array or object in PHP?', None, 'json_decode() parses a JSON string.'),
 ('Which function returns the length of a string in PHP?', None, 'strlen($s) returns the string length.'),
 ('Which function splits a string into an array by a delimiter?', None, "explode(',', $text) splits a string into an array."),
 ('Which operator checks for identical value and type in PHP?', None, '=== checks both value and data type.'),
 ('Which modern built-in PHP extension provides safe database connections?', None, 'PDO supports prepared statements.'),
 ('Which function converts all letters in a string to lowercase in PHP?', None, 'strtolower($s) converts a string to lowercase.'),
 ('Which function appends an element to the end of an array in PHP?', None, 'array_push($arr, $val) appends an element.'),
])
QUIZ_EN["c"].extend([
 ('Which function frees memory allocated by malloc()?', None, 'free(ptr) returns heap memory to the system.'),
 ('Which header is required for string functions such as strlen and strcpy?', None, '<string.h> declares string functions.'),
 ('Which operator returns the size in bytes of a data type?', None, 'sizeof(int) returns the size in bytes.'),
 ('Which keyword defines a composite data structure in C?', None, 'struct groups variables into a single record.'),
 ('Which pointer value indicates that a pointer points nowhere?', None, 'NULL is the null pointer constant.'),
 ('Which function from <string.h> compares two strings?', None, 'strcmp(a, b) returns 0 when both strings are equal.'),
 ('Which preprocessor directive defines a macro or constant?', None, '#define NAME value runs before compilation.'),
 ('Which operator accesses a struct member through a pointer?', None, 'ptr->field is equivalent to (*ptr).field.'),
 ('Which printf format specifier prints a single character (char)?', None, '%c prints a single character.'),
 ('Which statement immediately exits a for or while loop?', None, 'break terminates the nearest enclosing loop.'),
 ('Which statement skips the rest of the current iteration?', None, 'continue jumps to the next loop iteration.'),
 ('Which return value from main() indicates success?', None, 'return 0; signals successful completion.'),
])
QUIZ_EN["cpp"].extend([
 ('Which header is needed to use std::vector?', None, '#include <vector> provides std::vector.'),
 ('Which method on std::vector adds an element at the end?', None, 'v.push_back(x) appends an element.'),
 ('Which method on std::vector returns the number of elements?', None, 'v.size() returns the element count.'),
 ('Which keyword allows a member function to be overridden in a derived class?', None, 'virtual enables dynamic dispatch.'),
 ('Which modern C++ smart pointer enforces sole ownership of an object?', None, 'std::unique_ptr deletes its object when out of scope.'),
 ('Which keyword defines a generic function or class in C++?', None, 'template <typename T> defines generic code.'),
 ('Which special method runs automatically when an object is destroyed?', None, 'A destructor starts with ~ and cleans up resources.'),
 ('What is the scope resolution operator in C++?', None, 'std::cout uses the :: operator.'),
 ('Which STL container stores unique elements in sorted order?', None, 'std::set stores unique keys in sorted order.'),
 ("Which C++11 keyword lets the compiler deduce a variable's type automatically?", None, 'auto deduces the type from its initializer.'),
 ('Which operator releases memory allocated with new?', None, 'delete frees an object allocated with new.'),
 ('Which standard C++ object reads input from the keyboard?', None, 'std::cin >> variable reads from standard input.'),
])
QUIZ_EN["csharp"].extend([
 ('Which keyword marks an asynchronous method that can use await in C#?', None, 'async is used with Task return types.'),
 ('Which LINQ method returns the first element or a default value if empty?', None, 'FirstOrDefault() avoids an exception when empty.'),
 ('Which symbol is used for inheritance or interface implementation in C#?', None, 'C# uses a colon (:).'),
 ('Which prefix enables string interpolation in C#?', None, 'The $ prefix enables interpolation inside { }.'),
 ('Which method on List<T> adds a new item?', None, 'list.Add(item) appends an element.'),
 ('Which property returns the number of elements in a C# array?', None, 'Arrays in C# use the Length property.'),
 ('Which generic collection stores key-value pairs in C#?', None, 'Dictionary<TKey, TValue> stores key-value pairs.'),
 ('Which keyword declares a namespace in C#?', None, 'namespace groups classes.'),
 ('Which operator provides a fallback value when the left expression is null?', None, 'The null-coalescing operator (??) checks for null.'),
 ('Which block in try/catch always executes to clean up resources?', None, 'finally always runs.'),
 ('Which statement automatically disposes an IDisposable object?', None, 'using calls Dispose() automatically.'),
 ('Which String method removes leading and trailing whitespace?', None, 'text.Trim() removes whitespace from both ends.'),
])
QUIZ_EN["react"].extend([
 ('What is the shorthand syntax for a React Fragment?', None, '<>...</> groups elements without an extra DOM node.'),
 ('Which hook holds a DOM reference without triggering a re-render?', None, 'useRef returns a persistent { current } object.'),
 ('When does useEffect(fn, []) with an empty array [] run?', ['Every second', 'Once on mount', 'Never', 'Only on unmount'], 'An empty dependency array [] runs the effect once on mount.'),
 ('Which event attribute handles a button click in JSX?', None, 'JSX uses camelCase event names such as onClick.'),
 ('Which hook shares data across the component tree without prop drilling?', None, 'useContext reads from a Context.'),
 ('Which hook caches an expensive calculation between renders?', None, 'useMemo(fn, deps) memoizes a computed value.'),
 ('Which hook memoizes a callback function so its reference stays stable?', None, 'useCallback(fn, deps) memoizes a callback function.'),
 ('How do you write a comment inside JSX?', ['<!-- comment -->', '{/* comment */}', '// comment', '## comment'], 'Use {/* ... */} inside JSX.'),
 ('Which event handler reads text changes on an <input> element in React?', None, 'onChange is called when the input value changes.'),
 ('What is an input whose value is driven by React state called?', None, 'A Controlled Component binds value to state.'),
 ('Which statement exports a component as the default export?', None, 'export default allows direct default import.'),
 ('Which array method is commonly used in JSX to render a list of elements?', None, 'array.map(item => <li key={item.id}>...</li>).'),
])
QUIZ_EN["mysql"].extend([
 ('Which command lists all databases on the MySQL server?', None, 'SHOW DATABASES; lists all databases.'),
 ('Which command selects a database to work with?', None, 'USE nama_db; sets the active database.'),
 ('Which command shows the column structure of a table?', None, 'DESCRIBE tabel; displays columns and types.'),
 ('Which clause skips a number of rows when paginating with LIMIT?', None, 'LIMIT 10 OFFSET 20 skips the first 20 rows.'),
 ('Which default MySQL storage engine supports ACID transactions and foreign keys?', None, 'InnoDB is the default transactional engine.'),
 ('Which MySQL function returns the current date and time?', None, 'NOW() returns the current date and time.'),
 ('Which constraint ensures all values in a column are distinct?', None, 'UNIQUE prevents duplicate values.'),
 ('Which constraint prevents a column from storing NULL values?', None, 'NOT NULL requires a non-null value.'),
 ('Which command quickly empties all rows from a table?', None, 'TRUNCATE TABLE removes all rows quickly.'),
 ('Which MySQL data type stores long text up to 65,535 characters?', None, 'TEXT stores long text.'),
 ('Which function replaces NULL with a fallback value in query results?', None, 'IFNULL(col, 0) returns 0 when col is NULL.'),
 ('Which transaction command permanently saves all changes?', None, 'COMMIT; finalizes the transaction.'),
])
