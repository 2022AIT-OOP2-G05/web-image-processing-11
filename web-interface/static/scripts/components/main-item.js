import { Components } from "./base-components.js";
import { ItemComponent } from "./item.js";
import { fetchBase } from "../utils/fetch.js";

export class MainComponent extends Components {
  constructor(templateId, hostId, newElId, afterBegin, url) {
    super(templateId, hostId, newElId, afterBegin);
    this.url = url;
    this._attach(afterBegin);
    this._configure();
    this._renderContent();
  }

  _configure() {
    this.contentEl = document.querySelector("ul");
    this.contentEl.id = "image-list";
  }

  async _renderContent() {
    const data = await fetchBase.fetch(this.url);

    data.forEach(
      (item) => new ItemComponent("img-item-template", this.contentEl.id, item)
    );
  }
}
