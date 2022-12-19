<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class AddNewColResultReportsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::table('result_reports', function (Blueprint $table) {
            $table->string('brand')->after('event_time')->nullable();
            $table->string('recipient_msisdn')->after('brand')->nullable();
            $table->string('sccp_gt')->after('recipient_msisdn')->nullable();
            $table->string('status')->after('sccp_gt')->nullable();
            $table->string('received_content')->after('status')->nullable();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        //
    }
}
