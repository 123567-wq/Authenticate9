describe('E-commerce Automation', () => {
  const product = 'Titan watch';

  context('Amazon', () => {
    it('should search and capture product details on Amazon', () => {
      cy.visit('https://www.amazon.in');
      cy.get('#twotabsearchtextbox').type(`${product}{enter}`);
      cy.get('.s-main-slot .s-result-item').first().within(() => {
        cy.get('h2 a span').invoke('text').as('amazonProductName');
        cy.get('.a-price-whole').invoke('text').as('amazonProductPrice');
        cy.get('h2 a').invoke('attr', 'href').as('amazonProductLink');
      });
      cy.get('@amazonProductLink').then(link => {
        cy.visit(link);
        cy.get('#add-to-cart-button').click();
        cy.get('#hlb-view-cart-announce').click();
        cy.get('input[name="proceedToRetailCheckout"]').click();
        cy.get('.a-button-input').click();
      });
    });
  });

  context('Flipkart', () => {
    it('should search and capture product details on Flipkart', () => {
      cy.visit('https://www.flipkart.com');
      cy.get('button').contains('✕').click();
      cy.get('input[title="Search for products, brands and more"]').type(`${product}{enter}`);
      cy.get('._1AtVbE').eq(2).within(() => {
        cy.get('a.IRpwTa').invoke('text').as('flipkartProductName');
        cy.get('div._30jeq3').invoke('text').as('flipkartProductPrice');
        cy.get('a.IRpwTa').invoke('attr', 'href').as('flipkartProductLink');
      });
      cy.get('@flipkartProductLink').then(link => {
        cy.visit(`https://www.flipkart.com${link}`);
        cy.get('button').contains('ADD TO CART').click();
        cy.get('button').contains('Place Order').click();
        cy.get('button').contains('CONTINUE').click();
      });
    });
  });
});
