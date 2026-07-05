[Документація](https://mermaid.js.org/syntax/gitgraph.html)

## TreeView

Both standard (`├──`, `└──`, `│`) and heavy (`┣━━`, `┗━━`, `┃`) Unicode variants are supported



```text
prodject/
├── app.py
└── pages/
		└── home.py
		├── pages1.py
		├── pages2.py
		...
		└── pagesN.py

```

```mermaid
treeView-beta
             "app.py" 
             "build"
```