# AI for Legal Assistance
___

In order to test this, keep the directory structure as :-
* ai-for-legal-assistance
* data
	* test
		* Add files for testing (I did it with 5)

___

TO DO :-
- [x] Getting good results on the current pre-process steps. 
	* The *resolve_abbrev.py* script does satisfactory, it is the criteria for adding the token to finalized result, which creates good data. ***(Done, tested)***
- [x] The *resolve_abbrev.py* cannot remove special characters which are written as it is, e.g., "\n \n \n \t\t" (Check final cell of _test.ipynb for more details) ***(It works perfectly now)***
- [x] Check errors in code run ***(Code runs perfectly, no errors)***
- [ ] Decide the use of tech. for law extraction, machine learning model (recommended by aryan) or regular expressions (very poor outcomes)
