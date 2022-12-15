export class Components {
  constructor(templateId, hostId, newElId, afterBegin) {
    this.template = document.getElementById(templateId);
    this.hostEl = document.getElementById(hostId);
    const importNode = document.importNode(this.template.content, true);
    this.el = importNode.firstElementChild;

    if (newElId) this.el.id = newElId;
    this._attach(afterBegin);
  }

  _attach(afterBegin) {
    this.hostEl.insertAdjacentElement(
      afterBegin ? "afterbegin" : "beforeend",
      this.el
    );
  }
}
