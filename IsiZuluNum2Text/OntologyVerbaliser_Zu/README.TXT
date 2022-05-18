Requirements:
- owlready-0.3
- if you want to use the GUI: tkinter

Running:
in the terminal, go to the directory where you unzipped the downloaded and uncompressed the zip file, type:
python start.py
or, if you have several python versions installed, something like
python3.4 start.py
This will start the isiZulu verbaliser with the GUI interface.
To run it without the GUI, then type 
python start.py -ui=False

To verbalise your ontology:
* IRI must end with ontology filename
  e.g., 
    IRI : http://www.semanticweb.org/mariakeet/ontologies/2016/10/testOntoisiZuluWithPW.owl
* Ontology path: use the whole path name to the directory wheter the ontology is stored.
  e.g., 
    /Users/yourHomeDirectory/OntologyVerbaliser_Zu/ModifiedOntology

* Errors are saved in the 'Error.txt' file

* Note: when adding new ontology vocabulary, the words may not yet be in the list of nouns or verb roots. Update nncParis.txt and vroots accordingly.

* Known limitations: in case of compound terms, it does not yet process terms with underscores, dashes, and CamelCase.
