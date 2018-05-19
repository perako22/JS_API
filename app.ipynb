{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# import libraries\n",
    "import numpy as np\n",
    "from flask import (\n",
    "    Flask,\n",
    "    render_template,\n",
    "    jsonify,\n",
    "    request,\n",
    "    redirect)\n",
    "\n",
    "#################################################\n",
    "# Flask Setup\n",
    "#################################################\n",
    "app = Flask(__name__)\n",
    "\n",
    "#################################################\n",
    "# Database Setup\n",
    "#################################################\n",
    "\n",
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine\n",
    "import pandas as pd\n",
    "\n",
    "engine=create_engine(\"sqlite:///DataSets/belly_button_biodiversity.sqlite\")\n",
    "\n",
    "session=Session(bind=engine)\n",
    "\n",
    "Base = automap_base()\n",
    "\n",
    "Base.prepare(engine, reflect=True)\n",
    "\n",
    "Samples = Base.classes.samples\n",
    "Metadata = Base.classes.samples_metadata\n",
    "OTU = Base.classes.otu"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n"
     ]
    },
    {
     "ename": "NotImplementedError",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNotImplementedError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-910e1b391562>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m     58\u001b[0m \u001b[1;32mif\u001b[0m \u001b[0m__name__\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m\"__main__\"\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     59\u001b[0m     \u001b[0mapp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mrun\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 60\u001b[1;33m     \u001b[1;32mraise\u001b[0m \u001b[0mNotImplementedError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNotImplementedError\u001b[0m: "
     ]
    }
   ],
   "source": [
    "# create route that renders index.html template\n",
    "@app.route(\"/\")\n",
    "def home():\n",
    "    return render_template(\"index.html\")\n",
    "\n",
    "@app.route(\"/names\")\n",
    "def names():\n",
    "    samples_query = session.query(Samples)\n",
    "    samples = pd.read_sql(samples_query.statement, samples_query.session.bind)\n",
    "    names=list()\n",
    "    for i in samples.to_dict().keys():\n",
    "        names.append(i)\n",
    "    names=names[1:]\n",
    "    return(jsonify(names))    \n",
    "\n",
    "@app.route(\"/otu\")\n",
    "def otu():\n",
    "    otu_query = session.query(OTU)\n",
    "    otu = pd.read_sql(otu_query.statement, otu_query.session.bind)\n",
    "    descriptions=otu.lowest_taxonomic_unit_found\n",
    "    return(jsonify(descriptions.to_dict()))  \n",
    "\n",
    "@app.route(\"/metadata/<sample>\")\n",
    "def metadata(sample):\n",
    "    sampleID=int(sample.split(\"_\")[1])\n",
    "    metadata_query = session.query(Metadata).filter(Metadata.SAMPLEID==sampleID)\n",
    "    metadata = pd.read_sql(metadata_query.statement, metadata_query.session.bind)\n",
    "    return(jsonify(metadata.to_dict()))   \n",
    "\n",
    "@app.route(\"/wfreq/<sample>\")\n",
    "def wfreq(sample):\n",
    "    sampleID=int(sample.split(\"_\")[1])\n",
    "    wfreq_query = session.query(Metadata).filter(Metadata.SAMPLEID==sampleID)\n",
    "    wfreq = int(pd.read_sql(wfreq_query.statement, wfreq_query.session.bind)['WFREQ'])\n",
    "    return(jsonify(wfreq))\n",
    "\n",
    "@app.route(\"/samples/<sample>\")\n",
    "def samples(sample):\n",
    "    samples_query = session.query(Samples)\n",
    "    all_samples = pd.read_sql(samples_query.statement, samples_query.session.bind)\n",
    "    data=all_samples[['otu_id',sample]]\n",
    "    data=data.loc[data[sample]>0]\n",
    "    data.columns=['otu_id','samples']\n",
    "    data=data.sort_values('samples',ascending=False)\n",
    "    otu_ids=[]\n",
    "    samples=[]\n",
    "    for i in range(0,len(data)):\n",
    "        otu_ids.append(str(data['otu_id'].iloc[i]))\n",
    "        samples.append(str(data['samples'].iloc[i]))\n",
    "    newdict={\n",
    "        \"otu_id\":otu_ids,\n",
    "        \"samples\":samples\n",
    "    }\n",
    "\n",
    "    return(jsonify(newdict))\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run()\n",
    "    raise NotImplementedError()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
