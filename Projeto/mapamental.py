from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='HTML, CSS, and JavaScript Mind Map')

# Set node attributes for different languages
html_color = 'lightblue'
css_color = 'lightgreen'
js_color = 'yellow'

# Add nodes and edges for HTML
dot.node('HTML', 'HTML', style='filled', fillcolor=html_color)
dot.node('Tags', 'Tags', style='filled', fillcolor=html_color)
dot.node('Attributes', 'Attributes', style='filled', fillcolor=html_color)
dot.node('Elements', 'Elements', style='filled', fillcolor=html_color)
dot.node('Forms', 'Forms', style='filled', fillcolor=html_color)
dot.node('Links', 'Links', style='filled', fillcolor=html_color)
dot.node('Lists', 'Lists', style='filled', fillcolor=html_color)

dot.edges(['HTMLTags', 'HTMLAttributes', 'HTMLElements', 'HTMLForms', 'HTMLLinks', 'HTMLLists'])

# Add nodes and edges for CSS
dot.node('CSS', 'CSS', style='filled', fillcolor=css_color)
dot.node('Selectors', 'Selectors', style='filled', fillcolor=css_color)
dot.node('Properties', 'Properties', style='filled', fillcolor=css_color)
dot.node('Box Model', 'Box Model', style='filled', fillcolor=css_color)
dot.node('Layout', 'Layout', style='filled', fillcolor=css_color)
dot.node('Responsive Design', 'Responsive Design', style='filled', fillcolor=css_color)

dot.edges(['CSSSelectors', 'CSSProperties', 'CSSBox Model', 'CSSLayout', 'CSSResponsive Design'])

# Add nodes and edges for JavaScript
dot.node('JavaScript', 'JavaScript', style='filled', fillcolor=js_color)
dot.node('Variables', 'Variables', style='filled', fillcolor=js_color)
dot.node('Functions', 'Functions', style='filled', fillcolor=js_color)
dot.node('Events', 'Events', style='filled', fillcolor=js_color)
dot.node('DOM Manipulation', 'DOM Manipulation', style='filled', fillcolor=js_color)
dot.node('AJAX', 'AJAX', style='filled', fillcolor=js_color)
dot.node('ES6+', 'ES6+', style='filled', fillcolor=js_color)

dot.edges(['JavaScriptVariables', 'JavaScriptFunctions', 'JavaScriptEvents', 'JavaScriptDOM Manipulation', 'JavaScriptAJAX', 'JavaScriptES6+'])

# Save and render the graph
dot.render('/mnt/data/HTML_CSS_JS_Mind_Map', format='png', cleanup=True)

# Visualize the graph
dot.view()