# LiaScript-Snippets

A snippet-plugin for [Atom](https://Atom.io) and [VSCode](https://code.visualstudio.com), easing the development of online courses with [LiaScript](https://LiaScript.github.io), and extended Markdown notation.

https://github.com/andre-dietrich/liascript-snippets

## Install



### VSCode

Simply go to the marketplace in [VSCode](https://code.visualstudio.com/) and search for "liascript-snippets".
To enable this snippet, you have to add the following configuration to your settings.json ... To get there, simply hit "Ctrl-Shift-P" and then type settings.

``` json
...

   "[markdown]": {
      "editor.tabCompletion": "on",
      "editor.quickSuggestions": true,
      "editor.snippetSuggestions": "top"
   },

...
```

For more information, check out the [help](https://aizac.herokuapp.com/install-visual-studio-code-with-liascript/).

### Atom

This has to be installed directly from the github repository.
Thus, got to the settings by hitting [Ctrl+Shift+P] and then type `settings` into the fuzzy search to get to the settings.
From there you have to select the install tab and insert `andre-dietrich/liascript-snippets` to install this plugin directly from GitHub.
Before that, make sure that you have [git](https://git-scm.com/downloads) installed.

If you need more information, then check out this [help](https://aizac.herokuapp.com/install-atom-with-liascript/).

#### Command Line


Install Atom 1.5 or newer

In the terminal, install the package via apm:

    `apm install liascript-snippets`

#### GUI

1. Install Atom 1.5 or newer
2. Launch Atom
3. Open Settings View using Cmd+, on macOS or Ctrl+, on other platforms
4. Click the Install tab on the left side
5. Enter `liascript-snippets` in the search box and press Enter
6. Click the "Install" button that appears

## Features

1. Start typing **lia** in your markdown document to see the extended help, that
   can be explored via fuzzy-searching. Hit Tab for inserting your selected
   snippet.
2. To ease the voice selection for different narrators, start typing **voice**
   and search through all possible voice settings.
3. Syntax highlighting help is offered if you start typing **hili** followed by
   your language of choice. Since LiaScript applies the ace-editor, there is a
   matching done between highlight.js and ace. You can select your language from
   highlight.js, but it will be translated into the text in parentheses.


**Screencast Lisascript-snippets and -preview**

![screencast](./preview.gif)<!--width= "100%" -->

## Related Projects

It is recommended to install also:

liascript-preview

* for [Atom](https://github.com/andre-dietrich/liascript-preview)
* for [VSCode](https://marketplace.visualstudio.com/items?itemName=LiaScript.liascript-preview)

A previewer plugin that renders your course directly within the Atom IDE or which starts the development server from VSCode.

## Recommended Projects

Since unicode is supported, you can also use any kind of Emoji, so installing
the following project is recommended...

https://atom.io/packages/autocomplete-emojis
