import { render, screen } from '@testing-library/react';
import App from './App';

describe('Test <App /> elements', () => {
  
  test('renders title', () => {
    render(<App />);
    const titleElement = screen.getByText(/Car app/i);
    expect(titleElement).toBeInTheDocument();
  });

  test('renders label', () => {
    render(<App />);
    const labelElement = screen.getByText(/Search a car name by plate/i);
    expect(labelElement).toBeInTheDocument();
  });

  test('renders button', () => {
    render(<App />);
    const buttonElement = screen.getByText(/Submit/i);
    expect(buttonElement).toBeInTheDocument()
  });

})