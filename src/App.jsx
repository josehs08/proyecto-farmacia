import { useState } from 'react';
import { PDFDocument } from 'pdf-lib';

export const App = () => {
  const [pdfText, setPdfText] = useState('');

  const handleFileChange = async (event) => {
    const file = event.target.files[0];
    if (file && file.type === 'application/pdf') {
      const buffer = await file.arrayBuffer();
      const pdfDoc = await PDFDocument.load(buffer);
      const textArray = [];
      
      for (let i = 0; i < pdfDoc.getPageCount(); i++) {
        const page = pdfDoc.getPage(i);
        const textContent = await page.getTextContent();
        
        for (const item of textContent.items) {
          textArray.push(item.str);
        }
      }

      setPdfText(textArray.join(' '));
    } else {
      setPdfText('Please upload a valid PDF file.');
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100">
      <h1 className="font-bold text-3xl mb-4">Welcome to React!</h1>
      <input type="file" accept="application/pdf" onChange={handleFileChange} className="mb-4 p-2 border border-gray-300 rounded" />
      <div className="max-w-sm bg-white p-4 rounded shadow-md">
        <h2 className="font-bold text-xl mb-2">PDF Content</h2>
        <p className="text-gray-700 whitespace-pre-line">
          {pdfText || 'No PDF content to display.'}
        </p>
      </div>
    </div>
  );
};