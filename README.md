# DockFlow translations

Help improve the wording you see in DockFlow for Mac. You can suggest a correction in your own language.

**[Suggest a correction](https://github.com/AppitStudio/dockflow-translations/issues/new?template=translation.yml)** if a label is confusing, cut off, or sounds unnatural. Include where you saw it and what you would use instead. For an English wording change or a new language, open an issue here too. Issues and screenshots are public, so crop out personal information.

## Use the offline editor

1. [Download the project ZIP](https://github.com/AppitStudio/dockflow-translations/archive/refs/heads/main.zip) and unzip it.
2. Double-click **Translation Editor.html**. It opens locally in a desktop browser. Click **Open translations folder…** and select the extracted **translations** folder.
3. Choose a language and file. Search by the wording you saw, compare it with English, then edit the translation. Download each edited file before closing the tab.
4. In your GitHub fork, open the matching language folder and use **Add file → Upload files** to replace the file with your download. Keep its original name (for example, `app.json`). Open a pull request to Appit Studio. You can also paste a single correction into the suggestion form above.

## Edit directly on GitHub

1. Open [German](translations/de), [Spanish](translations/es), or [Japanese](translations/ja). The matching [English files](translations/en) give the source text.
2. Choose the file for the screen. `app.json` covers most of DockFlow, `core.json` covers shared actions and errors, `permissions.json` covers the macOS permission explanation, `focus.json` covers the Focus filter, and `shortcuts.json` covers Siri and Spotlight phrases.
3. Search for the text, click the pencil on GitHub, and edit its value. Keep the key, plural forms, placeholders such as `%@`, `%arg`, and `${applicationName}`, and Markdown formatting. Some entries use identifiers as keys, with the readable English in the corresponding English file.
4. Open a pull request and mention the screen and the reason for the edit. Appit Studio reviews suggestions and includes accepted wording in a subsequent app build.

To see a translation on a Mac, open **System Settings → General → Language & Region → Applications**, add DockFlow, choose the language, and reopen the app. Use a build that includes the language.

For account, license, or purchase questions, use [private DockFlow support](https://dockflow.appitstudio.com/support).

## License and attribution

DockFlow translations © Appit Studio and contributors, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). This license applies to the materials published in this repository. The DockFlow application is distributed separately. By submitting proposed translation text, you agree to contribute it under the same license. [Contributor history](https://github.com/AppitStudio/dockflow-translations/graphs/contributors).
