<?php

$installer = $this;
$installer->startSetup();

// Link directory category table
                    /*<movie>
                        <table>youn_movies_movie</table>
                    </movie>
                    <celebrity>
                        <table>youn_movies_celebrity</table>
                    </celebrity>
                     <moviem2m>
                        <table>youn_movies_moviem2m</table>
                    </moviem2m>*/
$tableName = $installer->getTable('youn_movies/movie');
// Check if the table already exists
if ($installer->getConnection()->isTableExists($tableName) != true) {
    $table = $installer->getConnection()
        ->newTable($installer->getTable('youn_movies/movie'))
        //movie id field
        ->addColumn('movie_id', Varien_Db_Ddl_Table::TYPE_INTEGER, null, array(
            'identity'  => true,
            'unsigned'  => true,
            'nullable'  => false,
            'primary'   => true,
        ), 'Type Id')
         //movie name
        ->addColumn('name', Varien_Db_Ddl_Table::TYPE_TEXT, 250, array(
            'nullable'  => true,
        ), 'Movie Name')
        //movie synopsis
        ->addColumn('synopsis', Varien_Db_Ddl_Table::TYPE_TEXT, 250, array(
            'nullable'  => true,
        ), 'Movie synopsis')
        //category parent - fiel
        ->addColumn('store_id', Varien_Db_Ddl_Table::TYPE_SMALLINT, null,
            array(
                'unsigned' => true,
                'nullable' => false,
                'default' => '0',
            ),
            'Store Id')
        ->addColumn('is_active', Varien_Db_Ddl_Table::TYPE_SMALLINT, null, array(
            'unsigned'  => true,
            'nullable'  => false,
            'default'   => '1',
        ), 'Is Active')
        ->setComment('Youn Movies movie table');
    $installer->getConnection()->createTable($table);
}

//create the youn_movies/m2m table to link movies to celebrities
$tableName = $installer->getTable('youn_movies/moviem2m');
// Check if the table already exists
if ($installer->getConnection()->isTableExists($tableName) != true) {
    $table = $installer->getConnection()
        ->newTable($installer->getTable('youn_movies/moviem2m'))
        //movie id field
        ->addColumn('m2m_id', Varien_Db_Ddl_Table::TYPE_INTEGER, null, array(
            'identity'  => true,
            'unsigned'  => true,
            'nullable'  => false,
            'primary'   => true,
        ), 'Type Id')
         //movie to celebrity link type (actor,producer, etc)
        ->addColumn('type', Varien_Db_Ddl_Table::TYPE_TEXT, 250, array(
            'nullable'  => true,
        ), 'm2m link type')
         //category parent - fiel
        ->addColumn('movie_id', Varien_Db_Ddl_Table::TYPE_INTEGER, null,
            array(
                'unsigned' => true,
                'nullable' => false,
                'default' => '0',
            ),
            'Movie id')
        ->addColumn('celebrity_id', Varien_Db_Ddl_Table::TYPE_INTEGER, null,
            array(
                'unsigned' => true,
                'nullable' => false,
                'default' => '0',
            ),
            'Movie id')
        ->addColumn('is_active', Varien_Db_Ddl_Table::TYPE_SMALLINT, null, array(
            'unsigned'  => true,
            'nullable'  => false,
            'default'   => '1',
        ), 'Is Active')
        ->setComment('Youn Movies movie table');
    $installer->getConnection()->createTable($table);
}

// Create the youn_movies/celebrity table
$tableName = $installer->getTable('youn_celebrity/celebrity');
// Check if the table already exists
if ($installer->getConnection()->isTableExists($tableName) != true) {
    $table = $installer->getConnection()
        ->newTable($tableName)
        ->addColumn('celebrity_id', Varien_Db_Ddl_Table::TYPE_INTEGER, null,
            array(
                'identity' => true,
                'unsigned' => true,
                'nullable' => false,
                'primary' => true,
            ),
            'Link Id'
        )
        ->addColumn('celebrity_name', Varien_Db_Ddl_Table::TYPE_TEXT, 255,
            array(),
            'Celebrity Bio'
        )
       ->addColumn('celebrity_bio', Varien_Db_Ddl_Table::TYPE_TEXT, 255,
            array(),
            'Celebrity Bio'
        )
        ->addColumn('link_url', Varien_Db_Ddl_Table::TYPE_TEXT, 100,
            array(),
            'Link URL'
        )
        ->addColumn('event_location', Varien_Db_Ddl_Table::TYPE_TEXT, 255,
            array(),
            'Event Location'
        )

        ->addColumn('created_at', Varien_Db_Ddl_Table::TYPE_TIMESTAMP, null,
            array(
                'nullable' => false,
            ),
            'Created At')
        ->addIndex($installer->getIdxName('youn_movies/celebrity', array('celebrity_id')),
            array('celebrity_id'))
        ;

    $installer->getConnection()->createTable($table);
}



$installer->endSetup();
