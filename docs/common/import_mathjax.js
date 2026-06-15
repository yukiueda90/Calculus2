// Create a script element for MathJax configuration
var mathjaxConfigScript = document.createElement('script');
mathjaxConfigScript.textContent = `
    MathJax = {
        tex: {
            inlineMath: [   // start/end delimiter pairs for in-line math
                ['$', '$']
            ],
        }
    };
`;

// Create a script element for MathJax
var mathjaxScript = document.createElement('script');
mathjaxScript.id = 'MathJax-script';
mathjaxScript.src = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js';
mathjaxScript.async = true;

// Append both script elements to the document's head
document.head.appendChild(mathjaxConfigScript);
document.head.appendChild(mathjaxScript);
