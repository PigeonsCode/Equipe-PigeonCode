export class TMenuLink extends HTMLElement {
  connectedCallback() {
    const title = this.getAttribute("title");
    const linkFunc = this.getAttribute("linkFunc");
    const linkUrl = this.getAttribute("linkUrl");
    this.innerHTML = ` <li class="nav-item border-start ps-2 border-3 ${
      window.location.pathname === "/" + linkUrl
        ? "border-primary"
        : "border-tertiary"
    }">
      <a href='${linkFunc}' class="nav-link ${
      window.location.pathname === "/" + linkUrl ? "active" : ""
    } text-secondary" aria-current="page">
        ${title}
      </a>
    </li>`;
  }
}
customElements.define("t-menu-link", TMenuLink);
