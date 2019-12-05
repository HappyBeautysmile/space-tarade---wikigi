/// <reference types="Cypress" />

context("Home", () => {
  beforeEach(() => {
    cy.visit("https://tradespace.store/");
    cy.get("div:nth-child(3) > button:nth-child(1)").click();

    cy.get("#input-24").type("daweihuang@g.ucla.edu");

    cy.get("#input-27").type("aaaaaa");

    cy.get("div.v-card__actions > button:nth-child(3)").click();
  });

  it("Search ", () => {
    cy.get("header > div > a:nth-child(3) > button").click();

    cy.get("#cover > form > div > div > input[type=text]").type("plaid");

    cy.get("#s-cover > button").click();

    cy.get("#myitem > div:nth-child(1)").click();

    cy.get(
      "#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__title.headline.grey.lighten-2 > div > div.col > div.v-list-item__title"
    ).contains("Plaid");

    cy.get("div > div.v-card__actions > button:nth-child(3)").click();
  });

  it("Check if items component exists ", () => {
    cy.get("header > div > a:nth-child(5) > button").click();

    cy.get("div > a:nth-child(2) > button").click();

    cy.get("div.row > li:nth-child(2)").click();

    cy.get(
      "div.v-card__title.headline.grey.lighten-2 > div > div.col > div.v-list-item__title"
    ).contains("Skateboard");

    cy.get("div.col > div:nth-child(2)").contains("Dawei Huang");

    cy.get("div.col > div:nth-child(3)").contains("Los Angeles");

    cy.get(
      "div.v-avatar.v-list-item__avatar.grey > div > div.v-responsive__content"
    );

    cy.get("div.v-card__text > div > div:nth-child(1) > img");

    cy.get("div.v-card__text > div > div:nth-child(2)").contains(
      /(foobar|Hawk)/
    );
  });

  it("Edit items ", () => {
    cy.get("header > div > a:nth-child(5) > button").click();

    cy.get("div > a:nth-child(2) > button").click();

    cy.get("div.row > li:nth-child(2)").click();

    cy.get("div.v-card__actions > button:nth-child(2) > span")
      .wait(1000)
      .click();

    cy.get("#textarea")
      .wait(1000)
      .clear()
      .type("foobar");

    cy.get("div:nth-child(6) > button").click();

    cy.get("header > div > a:nth-child(5) > button").click();

    cy.get("div > a:nth-child(2) > button").click();

    cy.get("div.row > li:nth-child(2)").click();

    cy.get("div.v-card__text > div > div:nth-child(2)").contains("foobar");

    cy.get(
      "#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__actions > button:nth-child(2)"
    )
      .wait(3000)
      .click();

    cy.get("#textarea")
      .wait(1000)
      .clear()
      .type("Tony Hawk used to own it.");
  });

  it("Trade Transaction ", () => {
    cy.get("header > div > a:nth-child(3) > button").click();

    cy.get("#cover > form > div > div > input[type=text]").type("tv");

    cy.get("#s-cover > button").click();

    cy.get("#myitem > div:nth-child(1)").click();

    cy.get(
      "#app > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__title.headline.grey.lighten-2 > div > div.col > div.v-list-item__title"
    ).contains("TV");

    cy.get("div > div.v-card__actions > button:nth-child(2)").click();

    cy.get("header > div > a:nth-child(5) > button").click();

    cy.get("#app > div > main > div > div > a:nth-child(3) > button")
      .wait(2000)
      .click();

    cy.get("div.card > div:nth-child(2) > div:nth-child(2)");

    cy.get(
      "#app > div > main > div > div > div:nth-child(4) > div:nth-child(1) > div > div"
    ).contains("Akaash");
  });
});
