// A lógica será mudada, conforme a rolagem de página, o link deve ficar ativo qnd se encontrar com o id de mesmo elemento

export class TScrollspyLink extends HTMLElement {
  connectedCallback() {
    const title = this.getAttribute("title");
    const id = this.getAttribute("id");
    this.innerHTML = ` <li class="custom-nav-item nav-item border-start ps-2 border-2 ">
      <a href='${id}' class="custom-nav-link nav-link " aria-current="page">
        ${title}
      </a>
    </li>`;
  }
}
customElements.define("t-scrollspy-link", TScrollspyLink);
