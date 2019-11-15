/// <reference types="Cypress" />

context("Home", () => {
  beforeEach(() => {
    cy.visit("http://localhost:8080/#/");
  });

  it("Register ", () => {
    cy.get("button.v-btn:nth-child(4)").click();
    cy.get(
      "#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__title > span"
    ).contains("User Profile:");
    cy.get(
      "#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__actions > button:nth-child(2) > span"
    ).click();
    cy.get(
      "#app > div.v-application--wrap > main > div > div > div > div > div:nth-child(4) > span"
    ).contains("Every time you buy something");
  });

  it("Search ", () => {
    cy.get("#app > div > header > div > a:nth-child(3) > button").click();
    cy.wait(100);
    cy.get(".col")
      .first()
      .click();
    cy.get("#app > div > main > div > div > div > li:nth-child(1)").click();
    cy.get(
      "#app > div > main > div > div > div > div > div > div:nth-child(2) > div.card-body > p"
    ).contains("Good shoes");
  });

  it("Account ", () => {
    cy.get("#app > div > header > div > a:nth-child(4) > button").click();
    cy.get(
      "#app > div > main > div > div > div > div.v-avatar.v-list-item__avatar.grey > div > div.v-image__image.v-image__image--cover"
    );
  });

  it("Start Trade ", () => {
    cy.get("#app > div > header > div > a:nth-child(5) > button").click();
    cy.get("#__BVID__30").type("blue{enter}");
    cy.get("#__BVID__30").type("adidas{enter}");
    cy.get("#__BVID__30").type("ecofriendly{enter}");
    cy.get(
      "#app > div > main > div > div > div:nth-child(4) > ul > button:nth-child(3)"
    ).click();
    cy.get(
      "#app > div > main > div > div > div:nth-child(4) > ul > button"
    ).should("have.length", 2);
  });
});
