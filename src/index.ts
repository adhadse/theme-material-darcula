// Copyright (c) Max Klein.
// Copyright (c) Anurag Dhadse
// Distributed under the terms of the Modified BSD License.

import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from "@jupyterlab/application";

import { IThemeManager } from "@jupyterlab/apputils";

/**
 * A plugin for @adhadse/theme-material-darcula
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: "@adhadse/theme-material-darcula:plugin",
  requires: [IThemeManager],
  activate: function(app: JupyterFrontEnd, manager: IThemeManager) {
    const style = "@adhadse/theme-material-darcula/index.css";

    manager.register({
      name: "Material Darcula",
      isLight: false,
      themeScrollbars: true,
      load: () => manager.loadCSS(style),
      unload: () => Promise.resolve(undefined)
    });
  },
  autoStart: true
};

export default plugin;
