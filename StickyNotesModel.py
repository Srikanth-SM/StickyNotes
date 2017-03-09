from flask import request, jsonify, render_template
import flask.views
import json
import sqlite3

# conn = sqlite3.connect('/Users/srikanth.s/StickyNote.db')

# conn=""
class ViewNotes(flask.views.MethodView):
    def get(self):
        notes=self.retrieveNotes()
        print "hai",notes
        # console.log("notes=",notes)
        return jsonify({
            'success': True,
            # notes is an array of dictionary which is returned from retrive notes function(title,description,priority)
            # mapping each and every value to the respective key from notes array
            'notesList': [{'ID':r[0],'title':r[1],'description':r[2],'priority':r[3]} for r in notes]
        })

    def retrieveNotes(cls):
        # global conn
        print "Inside retrive Notes"
        conn = sqlite3.connect('/Users/srikanth.s/StickyNote.db')
        c=conn.cursor()
        rows = c.execute(
            'SELECT * FROM NOTES'
        )
        # convert the rows to a  list
        allnotes_list=list(rows)
        print "rows==",list(rows)
        # ll= [{'title':r[0],'description':r[1],'priority':r[2]} for r in list(rows)]
        # for r in list(rows):
        #     print "r=",r

        # print "ll=",ll
        conn.commit()
        conn.close()
        # print ll
        return (allnotes_list)
        # pass





class AddNotes(flask.views.MethodView):


    def post(self):
        args = json.loads(request.data)
        print args
        self.add_item(args)
        return jsonify({ 'success': True })

    def add_item(cls,notes):
        # global conns
        conns = sqlite3.connect('/Users/srikanth.s/StickyNote.db')
        print conns
        c = conns.cursor()
        rows=[]
        if (notes):
            print "notes=",notes
            rows.append(notes['title'])
            rows.append(notes['description'])

            rows.append(notes['priority'])

        c.execute('''create table if not exists NOTES (title text,description text,priority int)''')
        # Insert a row of data
        if rows:
            c.execute('INSERT INTO NOTES (title,description,priority) VALUES (?,?,?)',tuple(rows))
        # c.execute('SELECT * FROM NOTES')
        print c
        # Save (commit) the changes
        conns.commit()
        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        conns.close()
