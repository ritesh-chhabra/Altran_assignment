from config import app, db, api


# handle 404 error with custom message
@app.errorhandler(404)
def not_found_error(error):
    return {"message": "API endpoint not found"}, 404

# handle 500 error with custom message
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return {"message": "Error in execution"}, 500