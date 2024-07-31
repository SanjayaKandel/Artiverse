import json
import base64
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
import requests
from Home .models import CartItem, OrderedItem
import datetime

def payment_success(request):
    data = request.GET.get('data')

    if data:
        try:
            decoded_data = base64.b64decode(data).decode('utf-8')
            parsed_data = json.loads(decoded_data)

            ref_id = parsed_data.get('transaction_code')
            oid = parsed_data.get('transaction_uuid')
            amount = parsed_data.get('total_amount').replace(",", "")

            if not ref_id or not oid or not amount:
                return HttpResponse("Invalid request parameters.")

            params = {
                'product_code': settings.ESEWA_MERCHANT_CODE,
                'total_amount': amount,
                'transaction_uuid': oid,
            }

            verification_url = f"{settings.ESEWA_VERIFY_URL}?product_code={params['product_code']}&total_amount={params['total_amount']}&transaction_uuid={params['transaction_uuid']}"

            try:
                response = requests.get(verification_url)
                response.raise_for_status()

                verification_response = response.json()
                if verification_response.get('status') == 'COMPLETE':
                    user = request.user
                    selected_item_ids = request.session.get('selected_item_ids', [])

                    if selected_item_ids:
                        # Debugging: print the selected item IDs
                        print(f"Selected item IDs: {selected_item_ids}")

                        # Fetch cart items to check if they exist
                        cart_items = CartItem.objects.filter(id__in=selected_item_ids, user=user)
                        print(f"Cart items to delete: {cart_items}")

                        # Delete the selected items
                        count, _ = CartItem.objects.filter(id__in=selected_item_ids, user=user).delete()
                        print(f"Number of items deleted: {count}")

                        # Update OrderedItems
                        OrderedItem.objects.filter(user=user, order_status='pending').update(order_status='completed')
                        OrderedItem.objects.filter(user=user, payment_completed=False).update(payment_completed=True)

                        # Clear selected items from session
                        del request.session['selected_item_ids']
                    else:
                        print("No selected item IDs found in session.")

                    return redirect('cart_view')
                else:
                    return HttpResponse("Payment Verification Failed!")

            except requests.RequestException as e:
                print(f"Error verifying payment: {e}")
                return HttpResponse("Payment Verification Failed due to an error.")

        except (json.JSONDecodeError, base64.binascii.Error) as e:
            print(f"Error decoding data: {e}")
            return HttpResponse("Invalid request data.")

    return HttpResponse("Invalid request parameters.")


def payment_failure(request):
    return HttpResponse("Payment Failed!")
