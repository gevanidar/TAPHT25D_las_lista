Feature: Navigering
  Som en användare av läslistan
  Vill jag kunna navigera till de olika delarna av sidan
  För att kunna använda sidans olika funktioner

  Background:
    Given att jag är på hemsidan

  Scenario Outline: Ska jag kunna navigera till de olika sidorna
    When jag trycker på knappen <knapp>
    Then bör jag se en div med <class>

    Examples:
      | artist        | class |
      | catalog   | catalog             |
      | add-book | form            |
      | favorites        |     favorites          |
      | statistics | stats            |

  Scenario: Naviering till Katalog
    When jag trycker på knappen catalog
    Then bör jag se en lista med 13 böcker

  Scenario: Naviering till Lägg till bok
    When jag trycker på knappen add-book
    Then bör jag se en label Titel
    And bör jag se en label Författare

  Scenario: Naviering till Mina böcker
    When jag trycker på knappen favorites
    Then bör jag se en test "När du valt, kommer dina favoritböcker att visas här."

  Scenario: Naviering till Statistik
    When jag trycker på knappen statistics
    Then bör jag se en test "När du valt, kommer dina favoritböcker att visas här."
