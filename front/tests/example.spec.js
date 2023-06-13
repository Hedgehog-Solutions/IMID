// @ts-check
const { test, expect } = require('@playwright/test');

test('has title', async ({ page }) => {
  await page.goto('http://localhost:3000');

  await expect(page).toHaveTitle(/IMID Data/);
});

test('access request page', async ({ page }) => {
  await page.goto('http://localhost:3000');

  // Click the get started link.
  await page.getByRole('link', ).click();

  await expect(page).toHaveURL(/.*access-request/);
});

test('login', async ({ page }) => {
  await page.goto('http://localhost:3000');

  await page.getByPlaceholder('login').fill('test');
  await page.getByPlaceholder('hasło').fill('test');

  await page.getByRole('button').click();

  await expect(page).toHaveURL(/.*dashboard/);
});

test('logout', async ({ page }) => {
  await page.goto('http://localhost:3000/dashboard');


  await page.getByText('Wyloguj').click();

  await expect(page).toHaveURL(/http:\/\/localhost:3000/);
});

test('back-to-dash', async ({ page }) => {
  await page.goto('http://localhost:3000/new-data');


  await page.getByText('cofnij').click();

  await expect(page).toHaveURL(/.*dashboard/);
});

