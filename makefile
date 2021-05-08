clean:
	@echo "Deleting all Jupyter Checkpoints"
	rm -rf **/.ipynb_checkpoints
	@echo "Deleting all PyCache Dirs"
	rm -rf **/__pycache__