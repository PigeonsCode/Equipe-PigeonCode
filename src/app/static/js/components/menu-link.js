export class TMenuLink extends HTMLElement {
  connectedCallback() {
    const title = this.getAttribute("title");
    const linkFunc = this.getAttribute("linkFunc");
    const linkUrl = this.getAttribute("linkUrl");
    this.innerHTML = ` <li class="custom-nav-item nav-item border-start ps-2 border-2 ${
      window.location.pathname === "/" + linkUrl
        ? "border-primary"
        : "border-tertiary"
    }">
      <a href='${linkFunc}' class="custom-nav-link nav-link ${
      window.location.pathname === "/" + linkUrl ? "active" : ""
    } " aria-current="page">
        ${title}
      </a>
    </li>`;
  }
}
customElements.define("t-menu-link", TMenuLink);
