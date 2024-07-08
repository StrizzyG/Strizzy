import zipfile
import os

# Create a directory structure for the React course
project_name = "react-kursus"
os.makedirs(f"{project_name}/public", exist_ok=True)
os.makedirs(f"{project_name}/src", exist_ok=True)

# index.html content
index_html_content = """<!DOCTYPE html>
<html lang="da">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lær at kode med React</title>
    <link rel="stylesheet" href="%PUBLIC_URL%/styles.css">
</head>
<body>
    <noscript>Du skal aktivere JavaScript for at kunne se denne applikation.</noscript>
    <div id="root"></div>
</body>
</html>
"""

# Write index.html
with open(f"{project_name}/public/index.html", "w") as file:
    file.write(index_html_content)

# App.js content
app_js_content = """import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header>
        <h1>Velkommen til React Kursus</h1>
        <nav>
          <ul>
            <li><a href="#introduction">Introduktion</a></li>
            <li><a href="#basics">React Grundlæggende</a></li>
            <li><a href="#components">Komponenter</a></li>
            <li><a href="#state">State og Props</a></li>
            <li><a href="#contact">Kontakt</a></li>
          </ul>
        </nav>
      </header>
      <main>
        <section id="introduction">
          <h2>Introduktion</h2>
          <p>Dette kursus vil lære dig grundlæggende React. Du vil lære at bygge forskellige komponenter og forstå React's syntaks og koncepter.</p>
        </section>
        <section id="basics">
          <h2>React Grundlæggende</h2>
          <article>
            <h3>Din første React Komponent</h3>
            <p>En React-komponent kan defineres som en funktion eller klasse.</p>
            <pre><code>function HelloWorld() {
  return <h1>Hello, World!</h1>;
}</code></pre>
          </article>
          <article>
            <h3>JSX</h3>
            <p>JSX er en syntax extension for JavaScript, som lader dig skrive HTML-lignende kode i dine JavaScript-filer.</p>
            <pre><code>const element = &lt;h1&gt;Hello, World!&lt;/h1&gt;;
ReactDOM.render(element, document.getElementById('root'));</code></pre>
          </article>
        </section>
        <section id="components">
          <h2>Komponenter</h2>
          <article>
            <h3>Funktionelle Komponenter</h3>
            <p>Funktionelle komponenter er JavaScript-funktioner, som returnerer JSX.</p>
            <pre><code>function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}</code></pre>
          </article>
          <article>
            <h3>Klasse Komponenter</h3>
            <p>Klasse komponenter er ES6 klasser, som udvider React.Component.</p>
            <pre><code>class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}</code></pre>
          </article>
        </section>
        <section id="state">
          <h2>State og Props</h2>
          <article>
            <h3>Props</h3>
            <p>Props er læse-only. De bruges til at sende data fra en komponent til en anden.</p>
            <pre><code>function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}</code></pre>
          </article>
          <article>
            <h3>State</h3>
            <p>State er private og fuldstændig kontrolleret af komponenten. De kan ændres over tid.</p>
            <pre><code>class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = {date: new Date()};
  }

  componentDidMount() {
    this.timerID = setInterval(
      () => this.tick(),
      1000
    );
  }

  componentWillUnmount() {
    clearInterval(this.timerID);
  }

  tick() {
    this.setState({
      date: new Date()
    });
  }

  render() {
    return (
      &lt;div&gt;
        &lt;h1&gt;Hello, world!&lt;/h1&gt;
        &lt;h2&gt;It is {this.state.date.toLocaleTimeString()}.&lt;/h2&gt;
      &lt;/div&gt;
    );
  }
}</code></pre>
          </article>
        </section>
      </main>
      <footer>
        <p>&copy; 2024 React Kursus. Alle rettigheder forbeholdes.</p>
      </footer>
    </div>
  );
}

export default App;
"""

# Write App.js
with open(f"{project_name}/src/App.js", "w") as file:
    file.write(app_js_content)

# App.css content
app_css_content = """body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.App {
  display: flex;
  flex-direction: column;
  flex: 1;
}

header {
  background: #333;
  color: #fff;
  padding: 1rem 0;
  text-align: center;
}

header nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  justify-content: center;
}

header nav ul li {
  margin: 0 1rem;
}

header nav ul li a {
  color: #fff;
  text-decoration: none;
}

main {
  flex: 1;
  padding: 2rem;
}

section {
  margin-bottom: 2rem;
}

h1, h2, h3 {
  color: #333;
}

pre {
  background: #333;
  color: #fff;
  padding: 1rem;
  overflow-x: auto;
}

footer {
  background: #333;
  color: #fff;
  text-align: center;
  padding: 1rem 0;
  margin-top: auto;
}
"""

# Write App.css
with open(f"{project_name}/src/App.css", "w") as file:
    file.write(app_css_content)

# index.js content
index_js_content = """import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
"""

# Write index.js
with open(f"{project_name}/src/index.js", "w") as file:
    file.write(index_js_content)

# index.css content (empty, but can be filled later)
index_css_content = """ """

# Write index.css
with open(f"{project_name}/src/index.css", "w") as file:
    file.write(index_css_content)

# Create a zip file of the project
zip_filename = f"{project_name}.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for root, dirs, files in os.walk(project_name):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), project_name))

# Provide the path to the zip file for download
zip_filename