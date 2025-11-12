export class TAccordion extends HTMLElement {
  connectedCallback() {
    const title = this.getAttribute("title");
    const accordionParent = document.getElementById(
      this.getAttribute("accordionParent")
    );
    const initialState = this.getAttribute("initialState") || "false";
    const isSolo = this.getAttribute("isSolo");
    const soloLink = this.getAttribute("soloLink");
    const collapseId = `collapse-${title.replace(/\s+/g, "-")}`;
    const isSidebarAdm = this.getAttribute("isSidebarAdm");


    const children = [...this.children];

    const item = document.createElement("div");
    item.className = "accordion-item";

    if (isSolo) {
      item.innerHTML = ` <h2 class="accordion-header ${isSidebarAdm ? "d-flex justify-content-between adm-accordion" : ""}">
        <a
          class="accordion-button sidebar-custom-button ${window.location.pathname == soloLink ? "" : "collapsed"
        }"
          type="button"
          href="${soloLink}"
        >
          ${title}
        </a>
        
      </h2>
      `;
    } else {
      item.innerHTML = `
      <h2 class="accordion-header">
        <button
          class="accordion-button ${initialState === "false" ? "collapsed" : ""
        }"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#${collapseId}"
          aria-expanded="${initialState}"
          aria-controls="${collapseId}"
        >
          ${title}
        </button>
      </h2>
      <div
        id="${collapseId}"
        class="accordion-collapse collapse ${initialState === "true" ? "show" : ""
        }"
       
      >
        <div class="accordion-body">
          
        </div>
      </div>
    `;

      const body = item.querySelector(".accordion-body");
      children.forEach((child) => body.appendChild(child));
    }

    accordionParent.appendChild(item);
    this.remove();
  }
}
customElements.define("t-accordion", TAccordion);
