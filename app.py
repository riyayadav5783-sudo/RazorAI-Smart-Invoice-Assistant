# RazorAI - Smart Invoice & Payment Assistant
# Project for Razorpay AI Buildathon

class RazorAIAssistant:
    def __init__(self):
        # Mock database for customer invoices and payments
        self.invoice_db = {
            "INV-1001": {"amount": "INR 4,500", "status": "Paid", "date": "2026-09-28"},
            "INV-1002": {"amount": "INR 12,000", "status": "Pending", "date": "2026-10-02"},
            "INV-1003": {"amount": "INR 1,200", "status": "Failed", "date": "2026-10-05"}
        }

    def process_query(self, query, invoice_id=None):
        """Processes customer queries regarding invoice and payment status"""
        if invoice_id and invoice_id in self.invoice_db:
            data = self.invoice_db[invoice_id]
            if "status" in query.lower():
                return f"Invoice {invoice_id} status is currently '{data['status']}'."
            elif "summary" in query.lower() or "details" in query.lower():
                return f"Invoice {invoice_id} details: Amount: {data['amount']}, Status: {data['status']}, Date: {data['date']}."
        
        return "I can help you check payment status, invoice details, or refund queries. Please provide a valid Invoice ID."

if __name__ == "__main__":
    bot = RazorAIAssistant()
    print("--- RazorAI Demo ---")
    print(bot.process_query("What is the status?", invoice_id="INV-1002"))
                  
