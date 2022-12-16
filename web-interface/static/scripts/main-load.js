import { MainComponent } from "./components/main-item.js";
import { HeaderComponent } from "./components/header.js";
export class Main {
  constructor(url) {
    new MainComponent("main-template", "app", "main", false, url);
    new HeaderComponent("header-template", "app", "header", true);
  }
}
