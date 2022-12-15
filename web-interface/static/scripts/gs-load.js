import { MainComponent } from "./components/main-item.js";
import { HeaderComponent } from "./components/header.js";
class Main {
  constructor() {
    new MainComponent("main-template", "app", "main", false, "/gs");
    new HeaderComponent("header-template", "app", "header", true);
  }
}

new Main();
