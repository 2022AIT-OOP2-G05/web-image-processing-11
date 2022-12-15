import { Components } from "./base-components.js";

export class HeaderComponent extends Components {
  constructor(templateId, newElId, afterBegin) {
    super(templateId, newElId, afterBegin);
    this._attach(afterBegin);
  }
}
