import { Components } from "./base-components.js";

export class ItemComponent extends Components {
  constructor(templateId, hostId, item) {
    super(templateId, hostId, item.id, true);
    this.item = item;
    this._attach(true);
    this._renderContent();
  }

  _renderContent() {
    this.el.querySelector(".file-name").textContent = this.item.name;
    this.el.querySelector("img").src = this.item.src;
  }
}
